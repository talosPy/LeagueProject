from django.urls import path
from . import views
from .views import player_list, add_player, delete_player_by_name

urlpatterns = [
    path('', player_list, name='player-list'),
    path('single/<str:player_name>/', views.single_player, name='single_player'),
    path('add/', add_player, name='add_player'),
    path('delete-by-name/', delete_player_by_name, name='delete-player-by-name'),



]