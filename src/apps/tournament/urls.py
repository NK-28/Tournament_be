from django.urls import path

from .views import tournamnet_list

urlpatterns = [
    path('', tournamnet_list, name='tournamnet_list'),
] 