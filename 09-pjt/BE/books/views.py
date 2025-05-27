from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Category
from rest_framework import status
from .serializers import BookListSerializer, BookSerializer, CategorySerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# Permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .utils import (
    recommend_books_from_fixture,
)


@api_view(['GET'])
def book_list(request):
    books = get_list_or_404(Book)
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_recommend(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    # 유사한 책 추천
    recommended_books = recommend_books_from_fixture(book)
    serializer = BookListSerializer(recommended_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bestseller_books(request):
    books = Book.objects.order_by('-customer_review_rank')[:10]
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)
