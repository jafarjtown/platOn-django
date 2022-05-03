from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics, filters
from account.models import User
from .models import Solution
from .serializers import SolutionSerializer, SolutionUpdateSerializer
import django_filters
import json
class SolutionCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)   
    def post(self, request):
        params = request.data.dict()
        try:
            if User.objects.filter(username = params['solver']).exists():
                params['solver'] = User.objects.get(username = params['solver'])
                solution = Solution.objects.create(**params)
                serializer = SolutionSerializer(solution)
                return Response(serializer.data)
            else:
                return JsonResponse({'message': 'No Solution with that username'})
        except Exception as e:
            return JsonResponse({'message':e.__str__()})
                     
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
    