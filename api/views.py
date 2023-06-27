from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializers
from .serializers import LoginSerializers
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate, login
import json
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['GET'])
def userApi( request):
    user = User.objects.all()
    serializer = UserSerializers(user, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 

@api_view(['POST'])
def loginApi(request):
    # permission_classes = (permissions.AllowAny,)
    serializer = LoginSerializers(data=request.data,
            context={ 'request': request })
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    password = serializer.validated_data['password']
    print(user)
    print(Token.key)
    login(request, user)
    return Response(status=status.HTTP_200_OK)