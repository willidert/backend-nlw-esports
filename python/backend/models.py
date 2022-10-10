from multiselectfield import MultiSelectField
import uuid
from django.db import models


class Game(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    bannerUrl = models.URLField()

    def __str__(self):
        return self.title


class Ad(models.Model):
    WEEK_DAYS = (
        (1, 'Domingo'),
        (2, 'SEGUNDA'),
        (3, 'TERCA'),
        (4, 'QUARTA'),
        (5, 'QUINTA'),
        (6, 'SEXTA'),
        (7, 'SABADO')
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    yearsPlaying = models.PositiveIntegerField()
    discord = models.CharField(max_length=200)
    weekDays = MultiSelectField(choices=WEEK_DAYS, max_length=7)
    hourStar = models.PositiveIntegerField()
    hourEnd = models.PositiveIntegerField()
    useVoiceChannel = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
