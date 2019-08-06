from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('rules', TemplateView.as_view(template_name='leaderboard/rules.html'), name='rules'),
    path('', views.Leaderboard.as_view(), name='leaderboard'),
    path('team', views.TeamView.as_view(), name='team'),
    path('team/leave', views.LeaveTeamView.as_view(), name='leave-team'),
    path('teams', views.CreateTeamView.as_view(), name='create-team'),
    path('teams/<int:pk>/join', views.JoinTeamView.as_view(), name='join-team'),
    path('submissions/create', views.CreateSubmissionView.as_view(), name='create-submission'),
]
