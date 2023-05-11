from django.db import models


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.player_name}'