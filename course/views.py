import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from course.models import CourseContent
from .serializers import CourseSerializer, Course
from account.models import User
# Create your views here.

class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        data = CourseSerializer(courses, many=True)
        return Response(data.data)
    
    def post(self, request):
        json_data = json.loads(request.body)
        dev = User.objects.get(id = json_data.get('user_id'))
        course = Course.objects.create(
            developer = dev, 
            text= json_data.get('text'), description = json_data.get('description'),
            title = json_data.get('title')
            )
        if json_data.get('contents'):
            for content in json_data.get('contents'):
                cc = CourseContent.objects.create(text = content.get('text'))
                if content.get('file'):
                    cc.file = content.get('file')
                course.contents.add(cc)
        return Response({'message':'Successfully created Course'})
        ...