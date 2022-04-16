import imp
from rest_framework import serializers

from account.models import User
from .models import Course


class CourseUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class CourseSerializer(serializers.ModelSerializer):
    developer = CourseUser()
    class Meta:
        model = Course
        fields = '__all__'
        
        depth = 2