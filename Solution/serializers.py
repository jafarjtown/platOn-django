
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
        # exclude = ['id']
        
        depth = 2
    
class SolutionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['content', 'title', 'summary','cover_img']