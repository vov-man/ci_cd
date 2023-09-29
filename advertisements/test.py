from http import client
from unittest import TestCase
from urllib import response

from rest_framework.test import APIClient


class TestApi(TestCase):
    def test_sample_view(self):
        client =APIClient()
        URL = 'api/'
        response = client.get(URL)
        assert response.status_code == 200