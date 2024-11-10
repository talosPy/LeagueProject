from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Match, LeagueTable  # Ensure LeagueTable is imported
from .serializers import MatchSerializer, LeagueTableSerializer
import random
from datetime import date, timedelta
from clubs.models import Club
from django.db.models import Sum, F
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


# List of team IDs based on your setup
team_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


@api_view(["POST"])
def add_match(request):
    """Add a match to the league."""
    serializer = MatchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def automate_matches(request):
    """Automatically create matches for specified teams and update league tables only if not already created."""
    teams = Club.objects.filter(id__in=team_ids)

    # Check if any matches have already been created
    if Match.objects.exists():
        return Response({"message": "Matches have already been generated."}, status=400)

    matches_created = []
    current_date = 0
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            home_team = teams[i]
            away_team = teams[j]
            match_date = date.today() + timedelta(days=current_date)
            match = Match.objects.create(
                home_team=home_team,
                away_team=away_team,
                match_date=match_date,
            )
        current_date += 7

    return Response({"matches_created": Match.objects.count()}, status=201)


@api_view(["POST"])
def play_fixture(request, fixture=0):
    fixture_date = date.today() + timedelta(days=fixture * 7)
    print("playing !!! : ", fixture_date)
    matches = Match.objects.filter(match_date=fixture_date)
    for match in matches:
        home_team = match.home_team
        away_team = match.away_team

        # Randomize scores
        goals_home = random.randint(0, 5)
        goals_away = random.randint(0, 5)

        # Update league standings for both teams
        match.goals_away = goals_away
        match.goals_home = goals_home
        match.save()
        update_league_table(home_team)
        update_league_table(away_team)
    return Response({"message": "fixture played! "})


def update_league_table(team):
    """Update league table for a given team based on match results."""
    matches = Match.objects.filter(home_team=team) | Match.objects.filter(
        away_team=team
    )

    wins = (
        matches.filter(goals_home__gt=F("goals_away")).count()
        if matches.filter(home_team=team).exists()
        else matches.filter(goals_home__lt=F("goals_away")).count()
    )
    losses = (
        matches.filter(goals_home__lt=F("goals_away")).count()
        if matches.filter(home_team=team).exists()
        else matches.filter(goals_home__gt=F("goals_away")).count()
    )
    draws = matches.filter(goals_home=F("goals_away")).count()

    goals_for = (
        matches.aggregate(Sum("goals_home"))["goals_home__sum"]
        if matches.filter(home_team=team).exists()
        else matches.aggregate(Sum("goals_away"))["goals_away__sum"]
    )
    goals_against = (
        matches.aggregate(Sum("goals_away"))["goals_away__sum"]
        if matches.filter(home_team=team).exists()
        else matches.aggregate(Sum("goals_home"))["goals_home__sum"]
    )

    # Update or create league table entry for the team
    LeagueTable.objects.update_or_create(
        team=team,
        defaults={
            "wins": wins,
            "losses": losses,
            "draws": draws,
            "goals_for": goals_for,
            "goals_against": goals_against,
        },
    )


@api_view(["GET"])
def list_matches(request):
    """List all matches."""
    matches = Match.objects.all()
    serializer = MatchSerializer(matches, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_league_table(request):
    """List the league table sorted by wins and draws."""
    league_table = LeagueTable.objects.all().order_by("-wins", "-draws")
    serializer = LeagueTableSerializer(league_table, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def generate_league_table(request):
    """Generate or update the league table based on current match results."""
    teams = Club.objects.all()
    for team in teams:
        update_league_table(team)

    return Response({"message": "League table updated successfully."}, status=200)


@api_view(["POST"])
def reset_league_table(request):
    """Reset matches and generate a new league table."""
    Match.objects.all().delete()  # Clear existing matches
    LeagueTable.objects.all().delete()  # Clear existing league table entries

    return Response(
        {"reset": "OK"}
    )  # automate_matches(request)  # Call automate_matches to generate new matches
