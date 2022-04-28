from tkinter.tix import Tree
from turtle import title
import django
from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, filters
from community.models import Tutorial
from community.serializers import TutorialSerializer
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
# Create your views here.


class TutorialFuncAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        return Response()
    
    def put(self, request):
        return Response()
    
    def delete(self, request):
        return Response()
    
    
    
class TutorialListAPIView(generics.ListAPIView):
    filter_params = ['id','tutor__username', 'title', 'body', 'created_on']
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    
    filter_backends = [filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = filter_params
    search_fields = filter_params
    
    
    
    
    # permission_classes = (IsAuthenticated,)
    
    
