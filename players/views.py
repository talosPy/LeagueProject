from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer
from django.shortcuts import get_object_or_404
from clubs.models import Club


@api_view(['GET'])
def player_list(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def single_player(request, player_name):
    player = get_object_or_404(Player, player_name=player_name)
    player_data = {
        'player_name': player.player_name,
        'position': player.position,
        'age': player.age,
        'is_injured': player.is_injured,
        'club': player.club.club_name,  
    }
    
    return Response(player_data)


@api_view(['POST'])
def add_player(request):
    if request.method == 'POST':
        club_id = request.data.get('club')
        try:
            club = Club.objects.get(id=club_id)
        except Club.DoesNotExist:
            return Response({'detail': 'Club not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(club=club)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
