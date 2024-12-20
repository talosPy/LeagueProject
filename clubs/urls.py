from django.urls import path
from . import views
from .views import club_list, add_club, single_club_view, delete_club_by_name

# LeagueTableView

urlpatterns = [
    # path('league-table/', LeagueTableView.as_view(), name='league-table'),
    path('', club_list, name='club-list'),
    path('add-club/', views.add_club, name='add-club'),
    path('single/<str:club_name>/', single_club_view, name='single-club'), 
    path('delete-by-name/', delete_club_by_name, name='delete_club_by_name'),
 



]

