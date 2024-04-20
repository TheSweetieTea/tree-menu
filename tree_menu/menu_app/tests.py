from http import HTTPStatus
from django.urls import reverse
from django.test import TestCase


class MenuItemTestCase(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse("menu_app:menu_view"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
