from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters


from .models import Tournament
from .serializers import TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
