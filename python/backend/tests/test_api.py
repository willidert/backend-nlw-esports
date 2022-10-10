from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class APITests(APITestCase):
    """
    Api tests
    """

    def test_list_games(self):
        """
        testa listagem de games
        """
        response = self.client.get(reverse('game-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)
