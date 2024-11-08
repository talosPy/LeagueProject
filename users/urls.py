from django.urls import path
from . import views  # Adjust the import path if necessary

urlpatterns = [
    # Other URL patterns
    path('user/', views.view_user, name='user'),
    path('register/', views.register, name='register'),

]
