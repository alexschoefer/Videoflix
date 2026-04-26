from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegistrationTests(APITestCase):

    def test_register_user_success(self):
        url = reverse('register')  # Name aus urls.py

        data = {
            "email": "test@test.com",
            "password": "12345678",
            "confirmed_password": "12345678"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email="test@test.com").exists())

    def test_register_password_mismatch(self):
        url = reverse('register')

        data = {
            "email": "test@test.com",
            "password": "12345678",
            "confirmed_password": "wrong"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_register_duplicate_email(self):
        User.objects.create_user(
            username="test@test.com",
            email="test@test.com",
            password="12345678"
        )

        url = reverse('register')

        data = {
            "email": "test@test.com",
            "password": "12345678",
            "confirmed_password": "12345678"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)