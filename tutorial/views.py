from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Tutorial
from .serializers import TutorialSerializer, TutorialImageSerializer
from PIL import Image, UnidentifiedImageError


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
        cover_image = request.FILES["cover_image"]
        # logic to check if valid image
        try: 
            trial_image = Image.open(cover_image)
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

class TutorialCreate(APIView):
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

