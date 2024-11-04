from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/', include('clubs.urls')),
    path('players/', include('players.urls')),
    path('matches/', include('matches.urls')),  # Include matches app URLs
]
