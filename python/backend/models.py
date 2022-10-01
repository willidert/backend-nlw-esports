import uuid
from django.db import models


class Game(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    bannerUrl = models.URLField()


class Ad(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    yearsPlaying = models.PositiveIntegerField()
    discord = models.CharField(max_length=200)
    weekDays = models.CharField(max_length=200)
    hourStar = models.PositiveIntegerField()
    hourEnd = models.PositiveIntegerField()
    useVoiceChannel = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
