from django.urls import path
from .views import emotion

urlpatterns = [
    path('emotions/',emotion),
]
