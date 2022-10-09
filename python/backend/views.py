from .models import Game, Ad
from .serializers import GameSerializer, AdSerializer, DiscordSerializer, AdCreateSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    #se der um GET em games/{:id}/ads
    @action(methods=['post', 'get'], detail=True, url_path='ads', url_name='ads_by_game')
    def get_ads_by_game(self, req, pk=None):
        if req.method == 'POST':
            data = req.data
            data['game'] = pk
            serializer = AdCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            ads = Ad.objects.filter(game=pk)
            serializer = AdSerializer(ads, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    #se der um POST em games/{:id}/ads
    # @action(methods=['post'], detail=True, url_path='ads', url_name='create_ad')
    # def create_ad(self, req, pk=None):
    #     data = req.data
    #     data['game'] = pk
    #     serializer = AdCreateSerializer(data=data)
    #     if serializer.is_valid():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdViewSet(viewsets.ViewSet):
    @action(methods=['get'], detail=True, url_path='discord', url_name='get_discord_by_ad')
    def get_discord_by_ad(self, req, pk=None):
        ad = Ad.objects.filter(id=pk).get()
        serializer = DiscordSerializer(ad)
        return Response(serializer.data, status=status.HTTP_200_OK)
