from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserCreateSerializer, UserSerializer
from .models import User
import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, generics
import json
from platon_backend.settings import SECRET_KEY, SIMPLE_JWT
from django.contrib.auth.hashers import make_password


class NoAuthorizationForPostOnly(IsAuthenticated):

    def has_permission(self, request, view):
        """
        If the request method is POST, then grant permission. Otherwise, authorization is required.
        """
        if request.method == "POST":
            return True
        return super().has_permission(request, view)


class UserAPIView(APIView):
    permission_classes = (NoAuthorizationForPostOnly,)

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data)
    
    def post(self, request):
        json_data = json.loads(request.body)
        json_data['password'] = make_password(json_data.get('password'))
        try:
            user = User.objects.create(**json_data)
            return Response({"success": True})
        except:
            return Response({"success": False})
    
    def put(self, request):
        try:
            json_body = json.loads(request.body)
            User.objects.filter(id = request.user.id).update(**json_body)
            return Response({"success": True})
        except Exception as e:
            print(e)
            return Response({'success': False, "message": "Unknown Error ocured"})
    
    def delete(self, request):
        request.user.delete()
        return Response({"success": True})
        ...

