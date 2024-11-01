from django.contrib import admin
from .models import Club

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'city', 'stadium', 'coach', 'is_active')
    search_fields = ('club_name', 'city')
    list_filter = ('is_active', 'city')
