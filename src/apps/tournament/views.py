from rest_framework import viewsets

from .models import PlayerTournamentScore, Tournament
from .serializers import PlayerTournamentScoreSerializer, TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class PlayerTournamentScorViewSet(viewsets.ModelViewSet):
    queryset = PlayerTournamentScore.objects.all()
    serializer_class = PlayerTournamentScoreSerializer
