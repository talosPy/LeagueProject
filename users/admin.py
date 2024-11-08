from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LeagueUser


class CustomUserAdmin(UserAdmin):
    model = LeagueUser
    list_display = ["username", "nickname", "age"]

    # Customize fields shown in the user change form
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("nickname", "age")}),
    )

    # Customize fields shown in the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("nickname", "age")}),
    )


admin.site.register(LeagueUser, CustomUserAdmin)
