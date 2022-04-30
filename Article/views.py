from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics, filters
from account.models import User
from .models import Article
from .serializers import ArticleSerializer, ArticleUpdateSerializer
import django_filters
import json
class ArticleCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)   
    def post(self, request):
        params = json.loads(request.body)
        try:
            if User.objects.filter(username = params['publisher']).exists():
                params['publisher'] = User.objects.get(username = params['publisher'])
                article = Article.objects.create(**params)
                serializer = ArticleSerializer(article)
                return Response(serializer.data)
            else:
                return JsonResponse({'message': 'No Publisher with that username'})
        except Exception as e:
            return JsonResponse({'message':e.__str__()})
                     
class ArticleListAPIView(generics.ListAPIView):
    filter_params = ['id', 'publisher__username', 'title', 'body', 'created_on', 'publish']
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = filter_params
    search_fields = filter_params   
    permission_classes = (IsAuthenticated,)   
    
     

class ArtileDetailDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)   
    
    
    
class ArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer
    permission_classes = (IsAuthenticated,)   
    