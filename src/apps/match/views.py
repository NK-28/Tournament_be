from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from rest_framework import viewsets

from apps.tournament.models import Tournament

from .forms import CreateMatchForm
from .models import Match
from .serializers import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class CreateMatchView(CreateView):
    template_name = "create_match.html"
    form_class = CreateMatchForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tournament = get_object_or_404(Tournament, pk=self.kwargs["tournament_id"])
        kwargs["tournament"] = tournament
        return kwargs

    def form_valid(self, form):
        tournament = get_object_or_404(Tournament, pk=self.kwargs["tournament_id"])
        player1 = form.cleaned_data["player1"]
        player2 = form.cleaned_data["player2"]

        if player1 == player2:
            raise ValidationError("Игрок не может играть сам с собой.")

        match = form.save(commit=False)
        match.tournament = tournament

        return redirect(
            reverse("tournament_detail", args=[self.kwargs["tournament_id"]])
        )
