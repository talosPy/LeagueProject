from django.db import models

class Club(models.Model):
    club_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.club_name
