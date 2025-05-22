from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ThreadListSerializer, ThreadSerializer
from .models import Thread
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
    book = Book.objects.get(pk=book_pk)
    if request.method == 'POST':
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # thread = serializer.save(user=request.user, book=book)
            thread = serializer.save(book=book)
            # generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
            
            # if generated_image_path:
            #     thread.cover_img = generated_image_path
            #     thread.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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
