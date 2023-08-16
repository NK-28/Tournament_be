from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from rest_framework import viewsets

from apps.tournament.models import PlayerTournamentScore, Tournament

from .forms import AddPlayerForm
from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class AddPlayerToTournamentView(FormView):
    template_name = "add_player_to_tournament.html"
    form_class = AddPlayerForm

    def form_valid(self, form):
        player = form.cleaned_data["player"]
        tournament = get_object_or_404(Tournament, pk=self.kwargs["tournament_id"])
        tournament.add_player(player)
        return redirect("tournament_detail", pk=tournament.pk)


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = "tournament_detail.html"


def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    player_tournament = Player.objects.filter(tournaments=tournament)
    player_scores = []

    for player in player_tournament:
        player_score = player.get_tournament_score(tournament)
        game_results = player.get_game_results(tournament)
        player_scores.append(
            {"player": player, "score": player_score, "game_results": game_results}
        )

    context = {
        "tournament": tournament,
        "player_scores": player_scores,
    }

    return render(request, "tournament_detail.html", context)
