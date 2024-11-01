from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Club
from players.models import Player
from .serializers import LeagueTableSerializer, ClubSerializer

# @api_view(['GET'])
# def league_table_view(request):
#     clubs = Club.objects.filter(is_active=True)
#     standings = []

#     for club in clubs:
#         # Initialize statistics
#         wins = draws = losses = goals_for = goals_against = 0
        
#         # Calculate stats based on match data
#         home_matches = Match.objects.filter(home_team=club, is_active=False)
#         away_matches = Match.objects.filter(away_team=club, is_active=False)

#         for match in home_matches:
#             if match.score:
#                 home_goals, away_goals = map(int, match.score.split('-'))
#                 goals_for += home_goals
#                 goals_against += away_goals
#                 if home_goals > away_goals:
#                     wins += 1
#                 elif home_goals < away_goals:
#                     losses += 1
#                 else:
#                     draws += 1

#         for match in away_matches:
#             if match.score:
#                 away_goals, home_goals = map(int, match.score.split('-'))
#                 goals_for += away_goals
#                 goals_against += home_goals
#                 if away_goals > home_goals:
#                     wins += 1
#                 elif away_goals < home_goals:
#                     losses += 1
#                 else:
#                     draws += 1

#         points = wins * 3 + draws
#         goal_difference = goals_for - goals_against

#         standings.append({
#             'club_name': club.club_name,
#             'wins': wins,
#             'draws': draws,
#             'losses': losses,
#             'goals_for': goals_for,
#             'goals_against': goals_against,
#             'goal_difference': goal_difference,
#             'points': points
#         })

#     # Sort standings by points, goal difference, then goals scored
#     standings.sort(key=lambda x: (x['points'], x['goal_difference'], x['goals_for']), reverse=True)

#     serializer = LeagueTableSerializer(standings, many=True)
#     return Response(serializer.data)



@api_view(['GET'])
def club_list(request):
    clubs = Club.objects.filter(is_active=True)  
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_club(request):
    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
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
