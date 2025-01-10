from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/', include('clubs.urls')),
    path('players/', include('players.urls')),
    path('matches/', include('matches.urls')),  # Include matches app URLs
    path('users/', include('users.urls')),  # Include matches app URLs
    
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

]
