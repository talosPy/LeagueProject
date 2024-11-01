from rest_framework import serializers
from matches.models import Match
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'



class LeagueTableSerializer(serializers.ModelSerializer):
    wins = serializers.IntegerField()
    draws = serializers.IntegerField()
    losses = serializers.IntegerField()
    goals_for = serializers.IntegerField()
    goals_against = serializers.IntegerField()
    goal_difference = serializers.IntegerField()
    points = serializers.IntegerField()

    class Meta:
        model = Club
        fields = [
            'club_name', 'wins', 'draws', 'losses', 
            'goals_for', 'goals_against', 'goal_difference', 'points'
        ]
