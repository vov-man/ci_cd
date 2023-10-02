from unittest import TestCase
from rest_framework.test import APIClient


class TestApi(TestCase):
    def test_sample_view(self):
        client = APIClient()
        URL = "api/test"
        response = client.get(URL)
        assert response.status_code != 200
