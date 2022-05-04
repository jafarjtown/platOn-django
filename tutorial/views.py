from PIL import Image, UnidentifiedImageError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, status
import django_filters
import json

from .models import Tutorial
from .serializers import *


class TutorialListAPIView(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = Tutorial.objects.all()
    serializer_class = TutorialListSerializer
    filter_params = [
        "id",
        "level",
        "time_to_complete",
        "main_lang",
        "add_lang", 
        "title",
        "tutor",
        "language",
        "summary",
        "overview",
        "requirements",
        "background",
        "steps",
        "created_on"
    ]
    filterset_fields = filter_params
    search_fields = filter_params 
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]


class TutorialCreateAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        json_data = json.loads(request.body)
        json_data['tutor'] = request.user.id

        if Tutorial.objects.filter(title=json_data['title'], tutor=request.user).exists():
            return Response(
                {
                    "message": "A tutorial with that title has already been created by you."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TutorialSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {
                "message": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

class TutorialUpdateAPIView(generics.UpdateAPIView):
    
    permission_classes = (IsAuthenticated,)
    queryset = Tutorial.objects.all()
    serializer_class = TutorialUpdateSerializer


class TutorialUpdateImageAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            tutorial = Tutorial.objects.get(pk=pk)
        except Tutorial.DoesNotExist:
            return Response(
                {
                    "message": "The tutorial with the given ID was not found."
                },
                status=status.HTTP_404_NOT_FOUND    
            )
            
        if tutorial.tutor == request.user:
            cover_image = {"cover_image": request.FILES["cover_image"]}
                
            serializer = TutorialImageSerializer(tutorial, data=cover_image)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "message": "Only the tutorial creator can change the cover image."
            },
            status=status.HTTP_403_FORBIDDEN    
        )


class TutorialDeleteAPIView(generics.RetrieveDestroyAPIView):
    
    permission_classes = (IsAuthenticated,)
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class TutorialReveiw(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        json_data = json.loads(request.body)
        json_data['tutor'] = request.user.id

        if Tutorial.objects.filter(title=json_data['title'], tutor=request.user).exists():
            return Response(
                {
                    "message": "A tutorial with that title has already been created by you."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TutorialSerializer(data=json_data)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(
            {
                "message": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class TutorialReveiwImage(APIView):
    
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try: 
            trial_image = Image.open(request.FILES["cover_image"])
            trial_image.verify()
            return Response({"message": "Valid"})
        except FileNotFoundError:
            return Response(
                {"message": "The image file could not be located."},
                status=status.HTTP_404_NOT_FOUND
            )
        except UnidentifiedImageError:
            return Response(
                {"message": "The image file could not be opened."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": e},
                status=status.HTTP_400_BAD_REQUEST
            )

