from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegistrationTests(APITestCase):
    """
    Test cases for user registration functionality. 
    This test class includes tests for successful registration, password mismatch, and duplicate email scenarios. 
    Each test case verifies the expected behavior of the registration endpoint and ensures that the appropriate responses are returned based on the provided input data.
    """
    def test_register_user_success(self):
        """
        Test successful user registration.
        This test case verifies that a user can successfully register with valid input data.
        It sends a POST request to the registration endpoint with a valid email, password, and confirmed password, and checks
        that the response status code is 201 (Created) and that the user is created in the database, indicating a successful registration.
        """
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
        """
        Test registration with password mismatch.
        This test case verifies that a user cannot register when the password and confirmed password do not match.
        It sends a POST request to the registration endpoint with a valid email but mismatched password and confirmed password, and checks
        that the response status code is 400 (Bad Request), indicating that the registration attempt was unsuccessful due to the password mismatch.
        """
        url = reverse('register')

        data = {
            "email": "test@test.com",
            "password": "12345678",
            "confirmed_password": "wrong"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_register_duplicate_email(self):
        """
        Test registration with duplicate email.
        This test case verifies that a user cannot register with an email that is already in use.
        It first creates a user with a specific email, then sends a POST request to the registration endpoint with the same email, and checks
        that the response status code is 400 (Bad Request), indicating that the registration attempt was unsuccessful due to the duplicate email.
        """
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