from django.contrib import admin

from .models import Player
from apps.tournament.models import Tournament


class TournamentInline(admin.TabularInline):
    model = Tournament.players.through


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name',) 
    search_fields = ('player_name',) 
    list_filter = ('player_name',) 
    inlines = (TournamentInline,)

admin.site.register(Player, PlayerAdmin)  
