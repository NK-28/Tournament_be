from django import forms

from .models import Player


class AddPlayerForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.all())
