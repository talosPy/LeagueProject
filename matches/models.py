from django.db import models
from clubs.models import Club

class Match(models.Model):
    home_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_matches')
    match_date = models.DateField()
    goals_home = models.IntegerField(null=True, blank=True)
    goals_away = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.match_date}"



class LeagueTable(models.Model):
    team = models.OneToOneField('clubs.Club', on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)

    def __str__(self):
        return self.team.name
