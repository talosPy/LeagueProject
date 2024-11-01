from django.contrib.auth.models import AbstractUser
from django.db import models


class LeagueUser(AbstractUser):
    nickname = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
