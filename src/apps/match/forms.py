from django import forms

from .models import Match


class CreateMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            "tournament",
            "game",
            "player1",
            "player2",
            "player1_score",
            "player2_score",
        ]

    def __init__(self, *args, **kwargs):
        tournament = kwargs.pop("tournament", None)
        super().__init__(*args, **kwargs)
        if tournament:
            self.fields["game"].queryset = tournament.games.all()
            self.fields["player1"].queryset = tournament.players.all()
            self.fields["player2"].queryset = tournament.players.all()
