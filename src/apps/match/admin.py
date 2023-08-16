from django.contrib import admin

from .models import Match, GameResult

admin.site.register(Match)


@admin.register(GameResult)
class GameResultAdmin(admin.ModelAdmin):
    list_display = ("player", "tournament", "match", "score")
