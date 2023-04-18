from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Tournament
from .serializers import TournamentSerializer


@api_view(['GET', 'POST'])
def tournamnet_list(request):
    if request.method == 'POST':
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    tournament = Tournament.objects.all()
    serializer = TournamentSerializer(tournament, many=True)
    return Response(serializer.data)