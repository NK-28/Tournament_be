from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters


from .models import Tournament
from .serializers import TournamentSerializer
from apps.users.permissions import FullAcessOrReadOnlyPermission


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [FullAcessOrReadOnlyPermission]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
