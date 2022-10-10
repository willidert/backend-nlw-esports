from django.test import TestCase

from ..models import Ad, Game


class GameTests(TestCase):
    """
    Models tests
    """

    def setUp(self) -> None:
        Game.objects.create(title='Teste 1', bannerUrl='https://teste.com')
        Game.objects.create(title='Teste 2', bannerUrl='https://teste.com')

    def test_create_ad(self):
        data = {
            "weekDays": [
                4,
                2
            ],
            "name": "William2",
            "discord": "will#123",
            "yearsPlaying": 2,
            "hourStar": 1200,
            "hourEnd": 1800,
            "useVoiceChannel": True
        }
        game = Game.objects.get(title='Teste 1')

        ad = Ad.objects.create(**data, game=game)

        self.assertEqual(str(ad), "William2")
        self.assertIsInstance(ad, Ad)
        self.assertEqual(ad.name, data['name'])
        self.assertEqual(Ad.objects.count(), 1)

    def test_game_has_ad(self):
        data = {
            "weekDays": [
                4,
                2
            ],
            "name": "William2",
            "discord": "will#123",
            "yearsPlaying": 2,
            "hourStar": 1200,
            "hourEnd": 1800,
            "useVoiceChannel": True
        }
        game = Game.objects.get(title='Teste 1')

        Ad.objects.create(**data, game=game)

        self.assertEqual(Ad.objects.filter(game=game.id).count(), 1)
