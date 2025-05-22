from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from rest_framework import status
from .serializers import BookListSerializer, BookSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# Permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def book_list(request):
    books = get_list_or_404(Book)
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)