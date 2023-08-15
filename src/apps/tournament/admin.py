from django.contrib import admin

from .models import Tournament, PlayerTournamentScore
from apps.match.models import Match


class PlayerTournamentScoreInline(admin.TabularInline):
    model = PlayerTournamentScore


class GameInline(admin.TabularInline):
    model = Tournament.games.through


class MatchInline(admin.TabularInline):
    model = Match


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        GameInline,
        PlayerTournamentScoreInline,
        MatchInline,
    ]
