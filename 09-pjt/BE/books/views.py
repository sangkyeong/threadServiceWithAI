from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_http_methods,
    require_safe,
    require_POST,
)
from django.contrib.auth.decorators import login_required

from accounts.models import Category
from .models import Book, Thread, Comment
from .forms import ThreadForm, CommentForm
from .utils import (
    generate_image_with_openai,
    recommend_books_from_fixture,
)


# Index 페이지
def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        "books" : books,
        "categories":categories
    }
    return render(request, 'books/index.html', context)

# 장르별 필터링
def filter_category(request):
    category_name = request.GET.get('category', '')
    category = ""

    if category_name:
        try:
            category = Category.objects.get(name=category_name)
            books = Book.objects.filter(category=category)
        except Category.DoesNotExist:
            books = []
    else:
        books = Book.objects.all()
    context = [
        {
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'cover': book.cover if book.cover else ""
        } for book in books
    ]

    return JsonResponse({'books':context})

@require_safe
def detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    # 유사한 책 추천
    recommended_books = recommend_books_from_fixture(book)

    context = {
        "book": book,
        "recommended_books": recommended_books,
    }
    return render(request, "books/detail.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def thread_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.book = book
            thread.user = request.user
            thread.save()

            generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
            if generated_image_path:
                thread.cover_img = generated_image_path
                thread.save()
                
            return redirect("books:thread_detail", book.pk, thread.pk)
    else:
        form = ThreadForm()
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "books/thread_create.html", context)


@login_required
@require_safe
def thread_detail(request, book_pk, thread_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    comment_form = CommentForm()
    context = {
        "book" : book,
        "thread": thread,
        "comment_form" : comment_form,
    }
    return render(request, "books/thread_detail.html", context)



@login_required
@require_http_methods(["GET", "POST"])
def thread_update(request, book_pk, thread_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    comment_form = CommentForm(request.POST)
    if thread.user == request.user:
        if request.method == "POST":
            form = ThreadForm(request.POST, request.FILES, instance=thread)
            if form.is_valid():
                form.save()  
                return redirect('books:thread_detail', book_pk=book.pk, thread_pk=thread.pk)
        else:
            form = ThreadForm(instance=thread)
    else :
        return redirect('books:index') 
    context = {
        "form": form,
        "book": book,
        "comment_form" : comment_form,
    }
    return render(request, "books/thread_update.html", context)


@login_required
@require_POST
def thread_delete(request, book_pk, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if thread.user == request.user:
        thread.delete()
    return redirect("books:detail", book_pk)


# 쓰레드 좋아요 비동기 처리
@require_POST
@login_required
def likes(request, book_pk, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)

    user = request.user
    if user in thread.likes.all():
        thread.likes.remove(user)
        liked = False
    else:
        thread.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': thread.likes.count(),
    })


# 쓰레드 댓글 비동기 처리
@require_POST
@login_required
def create_comment(request, book_pk, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.thread = thread
        comment.save()
        return JsonResponse({
            "id": comment.pk,
            "content": comment.content,
            "username": comment.user.username,
            "is_mine": True
        })
    return JsonResponse({"error": "Invalid form"}, status=400)

@require_POST
@login_required
def delete_comment(request, book_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
        return JsonResponse({"deleted": True})
    return JsonResponse({"error": "권한 없음"}, status=403)