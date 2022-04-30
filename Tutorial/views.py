from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, filters
from account.models import User
from .models import Tutorial
from .serializers import TutorialSerializer
import django_filters
import json
# Create your views here.

class TutorialFuncAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        params = json.loads(request.body)
        try:
            if User.objects.filter(username = params['tutor']).exists():
                params['tutor'] = User.objects.get(username = params['tutor'])
                tutorial = Tutorial.objects.create(**params)
                serializer = TutorialSerializer(tutorial)
                return Response(serializer.data)
            else:
                return JsonResponse({'message': 'No Tutor with that username'})
        except:
            return JsonResponse({'message':'Error occured'})
        return Response()
    
    def put(self, request, pk):
        
        update = json.loads(request.body)
        try:
            if Tutorial.objects.filter(id = pk).exists():
                print('here')
                tutorial = Tutorial.objects.filter(id = pk).update(**update)
                serializer = TutorialSerializer(tutorial)
                return Response(serializer.data)
            else:
                return JsonResponse({'message':'no Tutorial with the provided ID'})
        except Exception as e:
            print(e.__str__())
            return JsonResponse({'message':e.__str__()})
                
            
    
    def delete(self, request, pk):
        if pk != None:
            tutorial = Tutorial.objects.get(id = pk)
            tutorial.delete()
            return JsonResponse({'message':'successfully deleted Item'})
        return JsonResponse({'message':'Error occured'})
        
    
    
    
class TutorialListAPIView(generics.ListAPIView):
    filter_params = ['id','tutor__username', 'title', 'body', 'created_on']
    queryset = Tutorial.objects.all()
   
    serializer_class = TutorialSerializer
    
    filter_backends = [filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = filter_params
    search_fields = filter_params
    
    