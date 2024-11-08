from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Club
from players.models import Player
from .serializers import LeagueTableSerializer, ClubSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def club_list(request):
    clubs = Club.objects.filter(is_active=True)  
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_club(request):
    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def single_club_view(request, club_name):
    club = get_object_or_404(Club, club_name=club_name)
    players = Player.objects.filter(club=club)
    players_data = [{'name': player.player_name, 'position': player.position, 'age': player.age, 'is_injured': player.is_injured} for player in players]
    data = {
        'club_name': club.club_name,  
        'city': club.city,
        'stadium': club.stadium,
        'coach': club.coach,
        'players': players_data
    }
    return Response(data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_club_by_name(request):
    if request.method == 'DELETE':
        club_name = request.data.get('club_name', '').strip()  # Get the club name from the request body
        try:
            club = Club.objects.get(club_name=club_name)  # Adjust according to your field name
            club.delete()
            return Response({'message': 'Club deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except Club.DoesNotExist:
            return Response({'error': 'Club not found.'}, status=status.HTTP_404_NOT_FOUND)
