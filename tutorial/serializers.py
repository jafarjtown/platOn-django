from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
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
            "steps"
        )

class TutorialImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ("cover_image",)