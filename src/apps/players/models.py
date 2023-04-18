import uuid
from django.db import models

from apps.tournament.models import Tournament


class Player(models.Model):
    player_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    player_name = models.CharField(max_length=250)
    tournaments = models.ManyToManyField(Tournament)

