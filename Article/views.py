
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics, filters, status

from helper.models import ProLang
from .models import Article
from .serializers import ArticleCreateSerializer, ArticleSerializer, ArticleUpdateSerializer, UserSerializer
import django_filters
class ArticleCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)   
    def post(self, request):
        if(type(request.data) == dict):
            params = request.data
        else: 
            params = request.data.dict()
        params['publisher'] = request.user.pk
        lang, _ = ProLang.objects.get_or_create(name=params['language'])
        params['language'] = lang.pk
        serializer = ArticleCreateSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'messages': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
                 
class ArticleListAPIView(generics.ListAPIView):
    filter_params = ['id', 'publisher__username','summary','language__name', 'title', 'created_on', 'publish']
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
    