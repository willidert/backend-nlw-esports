from rest_framework import serializers
from .models import Ad, Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class AdSerializer(serializers.ModelSerializer):
    weekDays = serializers.MultipleChoiceField(choices=Ad.WEEK_DAYS)
    class Meta:
        model = Ad
        exclude = [
            "game",
            "discord",
            "createdAt"
        ]

class AdCreateSerializer(serializers.ModelSerializer):
    weekDays = serializers.MultipleChoiceField(choices=Ad.WEEK_DAYS)
    class Meta:
        model = Ad
        fields = '__all__'

class DiscordSerializer(serializers.Serializer):
    discord = serializers.CharField(max_length=200)
