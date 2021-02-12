from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse
from .models import Emotions
from .serializers import EmotionSerializer

# Create your views here.
def emotion(request):
    if request.method == 'GET':
        emotions = Emotions.objects.all()
        serialized = EmotionSerializer(emotions, many=True)
        return JsonResponse(serialized.data, safe=False)
