from django.db import models

from apps.game.models import Game
from apps.players.models import Player
from apps.tournament.models import PlayerTournamentScore, Tournament


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player1 = models.ForeignKey(
        Player, related_name="matches_as_player1", on_delete=models.CASCADE
    )
    player2 = models.ForeignKey(
        Player, related_name="matches_as_player2", on_delete=models.CASCADE
    )
    player1_score = models.PositiveIntegerField(default=0)
    player2_score = models.PositiveIntegerField(default=0)
    winner = models.ForeignKey(
        Player,
        related_name="matches_won",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.player1} vs {self.player2}"

    def save(self, *args, **kwargs):
        if self.player1_score > self.player2_score:
            self.winner = self.player1
        elif self.player2_score > self.player1_score:
            self.winner = self.player2

        super().save(*args, **kwargs)

        self.update_player_scores()

    def update_player_scores(self):
        if self.winner == self.player1:
            player1_score = self.tournament.get_points_for_win()
            player2_score = self.tournament.get_points_for_loss()
        elif self.winner == self.player2:
            player1_score = self.tournament.get_points_for_loss()
            player2_score = self.tournament.get_points_for_win()
        else:
            player1_score = self.tournament.get_points_for_draw()
            player2_score = self.tournament.get_points_for_draw()

        GameResult.objects.update_or_create(
            player=self.player1,
            tournament=self.tournament,
            match=self,
            defaults={"score": player1_score},
        )

        GameResult.objects.update_or_create(
            player=self.player2,
            tournament=self.tournament,
            match=self,
            defaults={"score": player2_score},
        )


class GameResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
