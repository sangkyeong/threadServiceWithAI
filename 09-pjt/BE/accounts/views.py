from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PureRegisterSerializer, UserSerializer, PureUpdateSerializer, passwordSerializer
from django.contrib.auth import get_user_model

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = UserSerializer(request.user)
    return Response(user.data)

@api_view(['GET'])
def user_profile(request, user_name):
    User = get_user_model()
    user = User.objects.get(username=user_name)
    serializer = UserSerializer(user, context={'request': request})
    return Response(serializer.data)

class SignupView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return []  # 회원가입은 누구나 가능
        return [IsAuthenticated()]
    
    def post(self, request):
        serializer = PureRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        print(request.data)
        serializer = PureUpdateSerializer(
            instance=request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원수정 성공!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    is_follow = False

    if request.user != person:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            is_follow = False
        else:
            person.followers.add(request.user)
            is_follow = True
    return Response({
        'follower_count' : person.followers.count(),
        'is_follow' : is_follow
    }, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = passwordSerializer(
            instance=user,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)