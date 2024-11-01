from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'position', 'age', 'club', 'is_injured')
    search_fields = ('player_name', 'position')
    list_filter = ('position', 'is_injured', 'club')
