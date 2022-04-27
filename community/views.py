from tkinter.tix import Tree
from turtle import title
from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from community.models import Tutorial
from community.serializers import TutorialSerializer

from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TutorialFilter(DjangoFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        
        filter_class = self.get_filter_class(view, queryset)
        
        if filter_class:
            print(request.query_params)
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset
    ...

class TutorialAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        # try to add add some query_params to the url
        # and print request.query_params
        # i want to use it in filtering the queryset
        queryset = Tutorial.objects.all()

        serializer = TutorialSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    
