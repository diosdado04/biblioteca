from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializer import CustomTokenObtainPairSerializer, CustomUserSerializer
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        print('user', username)
        print('password', password)
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({'token': login_serializer.validated_data.get('access'),'refresh-token': login_serializer.validated_data.get('refresh'),'user': user_serializer.data,'message': 'Inicio sesión exitoso'}, status=status.HTTP_200_OK)
            return Response({'error 1': 'Contraseña o nombre de usuario incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error 2': 'Contraseña o nombre de usuario incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)