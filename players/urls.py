from django.urls import path
from . import views
from .views import player_list, add_player

urlpatterns = [
    path('', player_list, name='player-list'),
    path('single/<str:player_name>/', views.single_player, name='single_player'),
    path('add/', add_player, name='add_player'),


]
