from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json
from .models import Tutorial
from account.models import User
from .serializers import TutorialSerializer, TutorialImageSerializer


class TutorialReveiw(APIView):
    pass


class TutorialAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # cover_image = request.FILES['cover_image']
        # request.data.pop("cover_image", None)
        # print(request.data)
        json_data = json.loads(request.body)
        json_data['tutor'] = request.user.id

        if Tutorial.objects.filter(title=json_data['title'], tutor=request.user).exists():
            return JsonResponse({
                "success": False,
                "message": "A tutorial with that title has already been created by you."
            })

        try:
            serializer = TutorialSerializer(data=json_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({
                    "success": True,
                })

            return JsonResponse({
                "success": False,
                "message": serializer.errors
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                "success": False,
                "message": e.message
            })
    
    def put(self, request, pk):
        try:
            tutorial = Tutorial.objects.get(pk=pk)
        except Tutorial.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Does not exist"
            })
            
        if tutorial.tutor == request.user:
            cover_image = {"cover_image": request.FILES["cover_image"]}
            try:
                serializer = TutorialImageSerializer(tutorial, data=cover_image)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({
                        "success": True,
                    })
                return JsonResponse({
                    "success": False,
                    "message": serializer.errors
                })

            except Exception as e:
                return JsonResponse({
                    "success": False,
                    "message": str(e)
                })
        return JsonResponse({
            "success": False,
            "message": "Only the tutorial creator can change the cover image."
        })

