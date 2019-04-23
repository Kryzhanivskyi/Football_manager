from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Match, Team, Statistic, Country, Tournament
from .serializers import MatchSerializer, TeamSerializer, StatisticSerializer, CountrySerializer, TournamentSerializer


class MatchView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('country__name', 'tour__tournament', 'host_team', 'guest_team', 'date_and_time', 'score_ended', 'round')
    ordering_fields = ('country__name',)
    search_fields = ('country__name', 'tour__tournament')


class TeamView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('name', 'score', 'president', 'coach', 'stadium', 'foundation', 'site', 'country__name')
    ordering_fields = ('score',)
    search_fields = ('name',)


class StatisticView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('name', 'games', 'goals', 'assists', 'goal_plus_pass', 'yellow_cards', 'red_cards', 'team')
    ordering_fields = ('name',)
    search_fields = ('team__name',)


class CountryView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class TournamentView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('county__name',)


def index(request):
    return render(request, 'index.html')




