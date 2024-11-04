from django.contrib import admin
from .models import Match

class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'match_date', 'goals_home', 'goals_away')
    search_fields = ('home_team__name', 'away_team__name')
    list_filter = ('match_date',)

admin.site.register(Match, MatchAdmin)
