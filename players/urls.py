from django.urls import path
from . import views


urlpatterns = [
    path("", views.player_list, name="player-list"),
    path("single/<str:player_name>/", views.single_player, name="single_player"),
    path("add/", views.add_player, name="add_player"),
    path("delete-by-name/", views.delete_player_by_name, name="delete-player-by-name"),
]
