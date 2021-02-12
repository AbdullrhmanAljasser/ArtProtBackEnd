from rest_framework import serializers
from .models import Emotions, ArtImage

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotions
        fields = ['id', 'title', 'description']

