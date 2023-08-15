from rest_framework import viewsets

from .models import Tournament, PlayerTournamentScore
from .serializers import TournamentSerializer, PlayerTournamentScoreSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
