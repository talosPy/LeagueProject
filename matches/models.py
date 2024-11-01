from django.db import models
from clubs.models import Club

class Match(models.Model):
    home_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_matches')
    match_date = models.DateField()
    score = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # fixture = 
    # season =

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.match_date}"
