from django.urls import path
from .views import list_matches, add_match, automate_matches, list_league_table, generate_league_table, reset_league_table, play_fixture

urlpatterns = [
    path('add/', add_match, name='add_match'),
    path('automate/', automate_matches, name='automate_matches'),
    path('list/', list_matches, name='list_matches'),
    path('league/', list_league_table, name='list_league_table'),  # New endpoint for league table
    path('generate-league-table/', generate_league_table, name='generate_league_table'),
    path('reset/', reset_league_table, name='reset_league_table'),
    path("play-fixture/<int:fixture>/", play_fixture, name="play_fixture"),



]
