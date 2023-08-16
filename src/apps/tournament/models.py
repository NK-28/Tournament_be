from django.core.exceptions import ValidationError
from django.db import models

from apps.game.models import Game
from apps.players.models import Player


class Tournament(models.Model):
    TOURNAMENT_TYPES = [
        ("single_elimination", "Single Elimination"),
        ("league", "League"),
    ]
    name = models.CharField(max_length=100)
    tournament_type = models.CharField(max_length=20, choices=TOURNAMENT_TYPES)
    games = models.ManyToManyField(Game)
    players_count = models.PositiveIntegerField()
    players = models.ManyToManyField(Player, through="PlayerTournamentScore")
    points_for_win = models.PositiveIntegerField(default=3)
    points_for_draw = models.PositiveIntegerField(default=1)
    points_for_loss = models.PositiveIntegerField(default=0)

    SINGLE_ELIMINATION = "single_elimination"
    LEAGUE = "league"

    def __str__(self):
        return self.name

    def clean(self):
        if self.players.count() > self.players_count:
            raise ValidationError("Too many players for this tournament.")

    def add_player(self, player):
        if self.players.count() >= self.players_count:
            raise ValidationError("Tournament is full.")
        self.players.add(player)

    def get_points_for_win(self):
        return self.points_for_win

    def get_points_for_draw(self):
        return self.points_for_draw

    def get_points_for_loss(self):
        return self.points_for_loss


class PlayerTournamentScore(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.player} - {self.tournament} - {self.points} points"
