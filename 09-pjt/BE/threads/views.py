from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ThreadListSerializer, ThreadSerializer, CommentSerializer
from .models import Thread, Comment
from books.models import Book


#테스트용

# from .utils import (
#     generate_image_with_openai,
#     recommend_books_from_fixture,
# )

@api_view(['GET', 'POST'])
def thread_list(request):
    if request.method == 'GET':
        threads = get_list_or_404(Thread)
        serializer = ThreadListSerializer(threads, many=True)
        return Response(serializer.data)
        

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def thread_create(request, book_pk):
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist:
        return Response({'msg': '책이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # thread = serializer.save(user=request.user, book=book)
            serializer.save(book=book, user=None)
            # generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
            
            # if generated_image_path:
            #     thread.cover_img = generated_image_path
            #     thread.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def thread_update(request, thread_pk):
    # book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    # thread.user == request.user and
    if  request.method == 'PATCH':
        serializer = ThreadSerializer(thread, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            # thread = serializer.save(user=request.user, book=book)
            thread = serializer.save(user=None)
            # generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
            
            # if generated_image_path:
            #     thread.cover_img = generated_image_path
            #     thread.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def thread_detail(request, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if request.method == 'GET':
        serializer = ThreadListSerializer(thread)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def thread_delete(request, thread_pk):
    try:
        thread = Thread.objects.get(pk=thread_pk)
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Thread.DoesNotExist:
        return Response({'msg': '쓰레드가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
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
    return Response({'msg': '쓰레드가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_comment(request, thread_pk):
    try:
        thread = Thread.objects.get(pk=thread_pk)
    except Thread.DoesNotExist:
        return Response({'msg': '쓰레드가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(thread=thread, user = request.user)
            serializer.save(thread=thread, user=None)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def delete_comment(request, comment_pk):
    try:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Comment.DoesNotExist:
        return Response({'msg': '해당 댓글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)


# # articles/views.py
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def article_list(request):
#     if request.method == 'GET':
#         articles = get_list_or_404(Thread)
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def article_detail(request, article_pk):
#     article = get_object_or_404(Thread, pk=article_pk)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return Response(serializer.data)

