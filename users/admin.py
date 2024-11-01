from django.contrib import admin
from .models import LeagueUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = LeagueUser
    list_display = ["username", "nickname", "age"]

admin.site.register(LeagueUser, CustomUserAdmin)
