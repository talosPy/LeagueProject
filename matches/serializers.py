from rest_framework import serializers
from .models import Match, LeagueTable

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class LeagueTableSerializer(serializers.ModelSerializer):
    club_name = serializers.CharField(source='team.club_name', read_only=True)  # Adjusted to use club_name

    class Meta:
        model = LeagueTable
        fields = ['club_name', 'wins', 'losses', 'draws', 'goals_for', 'goals_against']
