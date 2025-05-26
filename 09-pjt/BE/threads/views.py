from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ThreadListSerializer, ThreadSerializer, CommentSerializer
from .models import Thread, Comment
from books.models import Book
from .utils import (
    generate_image_with_openai,
    comment_openai
)

@api_view(['GET', 'POST'])
def thread_list(request):
    if request.method == 'GET':
        threads = Thread.objects.all()
        serializer = ThreadListSerializer(threads, many=True)
        return Response(serializer.data)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def thread_create(request, book_pk):
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist:
        return Response({'msg': '책이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    
    serializer = ThreadSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        thread = serializer.save(user=request.user, book=book)
        # 스레드 생성형 이미지 제작
        # generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
        
        # if generated_image_path:
        #     thread.cover_img = generated_image_path
        #     thread.save()
        thread.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def thread_update(request, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)

    if request.user != thread.user:
        return Response({'authMsg': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = ThreadSerializer(thread, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        thread = serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
@permission_classes([AllowAny])
def thread_detail(request, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    serializer = ThreadListSerializer(thread, context={'user': request.user})
    return Response(serializer.data)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def thread_delete(request, thread_pk):
    try:
        thread = Thread.objects.get(pk=thread_pk)
        if request.user != thread.user:
            return Response({'msg': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Thread.DoesNotExist:
        return Response({'msg': '쓰레드가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    
    user = request.user
    if user in thread.likes.all():
        thread.likes.remove(user)
    else:
        thread.likes.add(user)
    return Response({
        "like_count": thread.likes.count(),
        "liked": user in thread.likes.all()
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, thread_pk):
    try:
        thread = Thread.objects.get(pk=thread_pk)
    except Thread.DoesNotExist:
        return Response({'msg': '쓰레드가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(thread=thread, user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # commentPass = comment_openai(request.data)
        # if not commentPass:
        #     serializer.save(thread=thread, user = request.user)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response({'msg': '욕설이 포함되어 있습니다. 커뮤니티 규정을 준수하세요!'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_pk):
    try:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user != comment.user and request.user != comment.thread.user:
            return Response({'msg': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Comment.DoesNotExist:
        return Response({'msg': '해당 댓글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)