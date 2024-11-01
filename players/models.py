from django.db import models
from clubs.models import Club

class Player(models.Model):
    player_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    is_injured = models.BooleanField(default=False)

    def __str__(self):
        return self.player_name
