import uuid
from django.db import models


class Tournament(models.Model):
    TournamentType = [
        ('K.O.','knockout'),
        ('group', 'Group')
        ]

    tournament_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    tournament_type = models.CharField(max_length=200, choices=TournamentType, blank=False)
    players_number = models.SmallIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Tournamnet: {self.tilte}, type: {tournament_type}, players: {players_number}'
