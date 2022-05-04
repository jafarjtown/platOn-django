from rest_framework import serializers
from account.models import User
from .models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
class ArticleSerializer(serializers.ModelSerializer):
    publisher = UserSerializer()
    class Meta:
        model = Article
        fields = '__all__'
        
        depth = 2
    
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['publisher', 'content', 'title', 'language', 'summary', 'cover_img']

class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['content', 'title', 'summary']