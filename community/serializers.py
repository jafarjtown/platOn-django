from rest_framework import serializers

from account.serializers import UserSerializer
from .models import Tutorial
class TutorialSerializer(serializers.ModelSerializer):
    tutor = UserSerializer()
    class Meta:
        model = Tutorial
        # fields = '__all__'
        exclude = ['id']
        
        depth = 2