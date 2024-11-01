from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'match_date', 'score', 'is_active')
    search_fields = ('home_team__club_name', 'away_team__club_name')
    list_filter = ('is_active', 'match_date')
