from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PureRegisterSerializer, UserSerializer, PureUpdateSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = UserSerializer(request.user)
    return Response(user.data)

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
        serializer = PureUpdateSerializer(
            instance=request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원수정 성공!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
