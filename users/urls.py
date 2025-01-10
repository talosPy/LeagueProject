from django.urls import path
from . import views


urlpatterns = [
    path("user/", views.view_user, name="user"),
    path("register/", views.register, name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
]
