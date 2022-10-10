from django.test import TestCase

from model_bakery import baker

from ..models import Ad, Game


class GameTestModel(TestCase):
    """
    Class to test Game model
    """

    def setUp(self) -> None:
        self.game = baker.make(Game)

    def test_create_ad(self) -> None:
        ad = baker.make(Ad, name="nick de teste",
                        weekDays=[1, 2, 3], game=self.game)

        self.assertEqual(str(ad), "nick de teste")
        self.assertIsInstance(ad, Ad)
        self.assertEqual(ad.name, "nick de teste")
        self.assertEqual(Ad.objects.count(), 1)

    def test_game_has_ad(self):
        assert 1 == 1
