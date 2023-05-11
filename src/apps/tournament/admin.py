from django.contrib import admin

from .models import Tournament
from apps.players.models import Player


class PlayerInline(admin.TabularInline):
    model = Player.tournaments.through


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('title', 'tournament_type', 'players_number', 'pub_date') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    # Добавляем поле players (many to many)
    inlines = (PlayerInline,)

# При регистрации модели Post источником конфигурации для неё назначаем
# класс TournamentAdmin


