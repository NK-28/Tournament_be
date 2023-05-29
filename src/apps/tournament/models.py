from django.db import models
from apps.players.models import Player

class Tournament(models.Model):
    TournamentType = [
        ('K.O.','Knockout'),
        ('group', 'Group')
        ]

    tournament_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=200)
    tournament_type = models.CharField(max_length=200, choices=TournamentType, blank=False)
    players_number = models.SmallIntegerField()
    players = models.ManyToManyField(Player, related_name='tournaments')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Tournamnet: {self.title}, type: {self.tournament_type}, players: {self.players_number}'
