
from rest_framework import serializers
from account.models import User
from .models import Solution

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
class SolutionSerializer(serializers.ModelSerializer):
    solver = UserSerializer()
    class Meta:
        model = Solution
        fields = '__all__'
        depth = 2
 
class SolutionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = [
            'solver',
            'content',
            'title',
            'summary',
            'source',
            'language',
            'cover_img'
        ]
    
class SolutionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['content', 'title', 'summary','cover_img']