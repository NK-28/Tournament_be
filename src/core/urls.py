from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.game.views import GameViewSet
from apps.match.views import CreateMatchView, MatchViewSet
from apps.players.views import (
    AddPlayerToTournamentView,
    PlayerViewSet,
    TournamentDetailView,
)
from apps.tournament.views import TournamentViewSet

router = routers.DefaultRouter()


router.register(r"games", GameViewSet)
router.register(r"players", PlayerViewSet)
router.register(r"tournaments", TournamentViewSet)
router.register(r"matches", MatchViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/v1/", include(router.urls)),
    path(
        "api/v1/tournament/<int:tournament_id>/add-player/",
        AddPlayerToTournamentView.as_view(),
        name="add_player_to_tournament",
    ),
    path(
        "api/v1/tournament/<int:pk>/",
        TournamentDetailView.as_view(),
        name="tournament_detail",
    ),
    path(
        "api/v1/tournament/<int:tournament_id>/create-match/",
        CreateMatchView.as_view(),
        name="create_match",
    ),
]
