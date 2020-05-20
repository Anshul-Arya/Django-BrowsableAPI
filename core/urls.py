from django.urls import path
from .views import game_list, game_detail

urlpatterns = [
    path('games/', game_list, name='list'),
    path('games/<int:pk>', game_detail, name='detail'),
]