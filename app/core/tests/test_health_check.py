""" Test for the health chekc api """

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTest(TestCase):
    """ Test the heaalth check API """

    def test_health_check(self):
        """ Test health check API """
        client = APIClient()
        url = reverse('health-check')
        res = client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
