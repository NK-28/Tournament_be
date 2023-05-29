from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.tournament.views import TournamentViewSet

router = routers.DefaultRouter()



router.register(r'tournaments', TournamentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]
