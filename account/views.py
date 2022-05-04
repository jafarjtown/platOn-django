
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import UserCreateSerializer, UserSerializer
from community import serializers
from .models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import json
from django.contrib.auth.hashers import make_password
from rest_framework import status, generics


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
        return Response(user.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if(type(request.data) == dict):
            json_data = request.data
        else:
            json_data = request.data.dict()
        serializer = UserCreateSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created" }, status=status.HTTP_201_CREATED)
        return Response({
                "messages": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request):
        try:
            if(type(request.data) == dict):
                json_data = request.data
            else:
                json_data = request.data.dict()
            User.objects.filter(id = request.user.id).update(**json_data)
            return Response({"success": True, "message": "update is successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, "message": "Unknown Error ocured"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        request.user.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)
        ...

class UserAllAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser)