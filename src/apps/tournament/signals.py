from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.match.models import Match


# @receiver(post_save, sender=Match)
# def update_player_scores(sender, instance, **kwargs):
#     if instance.winner:
#         instance.winner.points += instance.win_points
#         instance.winner.save()
