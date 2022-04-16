from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer
from .models import User
import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
import json
from platon_backend.settings import SECRET_KEY, SIMPLE_JWT
from django.contrib.auth.hashers import make_password
class Login(APIView):
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        user = UserSerializer(request.user)
        return Response(user.data)
    
    def post(self, request):
        json_data = json.loads(request.body)
        json_data['password'] = make_password(json_data.get('password'))
        user = User.objects.create(**json_data)
        return Response({"successfully": True})

class Home(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        users = User.objects.all()
        data = UserSerializer(users, many=True)
        return Response(data.data)