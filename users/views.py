from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import LeagueUser
from .serializers import LeagueUserSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(["POST"])
def register(request):
    user = LeagueUser.objects.create_user(
        username=request.data["username"],
        email=request.data["email"],
        password=request.data["password"],
    )
    user.is_active = True
    user.is_staff = False
    user.save()
    return Response("Added New User, Hooray")


@api_view(["GET"])
def view_user(request):
    if not request.user.is_authenticated:
        return Response(
            {"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
        )

    serializer = LeagueUserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
