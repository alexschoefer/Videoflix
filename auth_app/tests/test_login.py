from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTests(APITestCase):
    """
    Test cases for user login functionality.
    This test class includes tests for successful login, login with wrong password, and login with an inactive user account. 
    Each test case verifies the expected behavior of the login endpoint and ensures that the appropriate responses are returned based on the provided credentials and user account status.
    """

    def setUp(self):
        """
        Set up a test user for login tests.
        This method creates a test user with a specified email and password, and sets the account to inactive or active.
        The created user is used in the subsequent login test cases to verify the login functionality under different scenarios.
        """
        self.user = User.objects.create_user(
            username="test@test.com",
            email="test@test.com",
            password="12345678",
            is_active=True
        )

    def test_login_success(self):
        """
        Test successful login with valid credentials.
        This test case verifies that a user can successfully log in with the correct email and password.
        It sends a POST request to the login endpoint with the valid credentials and checks 
        that the response status code is 200 (OK) and that an access token is included in the response cookies, indicating a successful login.
        """
        url = reverse('login')

        data = {
            "email": "test@test.com",
            "password": "12345678"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.cookies)

    def test_login_wrong_password(self):
        """
        Test login with incorrect password.
        This test case verifies that a user cannot log in with an incorrect password.
        It sends a POST request to the login endpoint with the correct email but an incorrect password, and checks 
        that the response status code is 400 (Bad Request), indicating that the login attempt was unsuccessful due to invalid credentials.
        """
        url = reverse('login')

        data = {
            "email": "test@test.com",
            "password": "wrong"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

    def test_login_inactive_user(self):
        """
        Test login with an inactive user account.
        This test case verifies that a user cannot log in if their account is inactive.
        It first sets the test user's account to inactive, then sends a POST request to the login endpoint with the correct email and password.        
        """
        self.user.is_active = False
        self.user.save()

        url = reverse('login')

        data = {
            "email": "test@test.com",
            "password": "12345678"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)