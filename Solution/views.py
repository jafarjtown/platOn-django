
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics, filters, status
from helper.models import ProLang
from .models import Solution
from .serializers import SolutionCreateSerializer, SolutionSerializer, SolutionUpdateSerializer
import django_filters
class SolutionCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)   
    def post(self, request):
        if(type(request.data) == dict):
            params = request.data
        else:
            params = request.data.dict()
        params['solver'] = request.user.pk
        lang, _ = ProLang.objects.get_or_create(name=params['language'])
        params['language'] = lang.pk
        serializer = SolutionCreateSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'messages': serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
              
class SolutionListAPIView(generics.ListAPIView):
    filter_params = ['id', 'solver__username','summary','language__name', 'title', 'created_on', 'approved']
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filter_backends = [filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = filter_params
    search_fields = filter_params   
    permission_classes = (IsAuthenticated,)   
    

class SolutionDetailDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = (IsAuthenticated,)   
    
    
    
class SolutionUpdateAPIView(generics.UpdateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionUpdateSerializer
    permission_classes = (IsAuthenticated,)   
    