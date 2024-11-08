from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer
from django.shortcuts import get_object_or_404
from clubs.models import Club
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def player_list(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def single_player(request, player_name):
    player = get_object_or_404(Player, player_name=player_name)
    player_data = {
        "player_name": player.player_name,
        "position": player.position,
        "age": player.age,
        "is_injured": player.is_injured,
        "club": player.club.club_name,
    }

    return Response(player_data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_player(request):
    if request.method == "POST":
        club_id = request.data.get("club")
        try:
            club = Club.objects.get(id=club_id)
        except Club.DoesNotExist:
            return Response(
                {"detail": "Club not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(club=club)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_player_by_name(request):
    if request.method == "DELETE":
        name = request.data.get(
            "name", ""
        ).strip()  # Get the player name from the request body
        try:
            player = Player.objects.get(player_name=name)  # Ensure to use player_name
            player.delete()
            return Response({"message": "Player deleted successfully!"}, status=204)
        except Player.DoesNotExist:
            return Response({"error": "Player not found."}, status=404)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=500
            )  # Return error message for unexpected issues
