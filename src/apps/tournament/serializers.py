from rest_framework import serializers
from .models import Tournament, PlayerTournamentScore


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class PlayerTournamentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerTournamentScore
        fields = '__all__'
