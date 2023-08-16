from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def get_tournament_score(self, tournament):
        from apps.tournament.models import PlayerTournamentScore

        return PlayerTournamentScore.objects.get(player=self, tournament=tournament)

    def get_game_results(self, tournament):
        from apps.match.models import GameResult

        return GameResult.objects.filter(player=self, tournament=tournament)
