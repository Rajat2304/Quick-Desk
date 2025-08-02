from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser
from rest_framework.authtoken.models import Token

class AccountTests(APITestCase):
    def test_register_user(self):
        """
        Ensure we can create a new user account.
        """
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'somepassword123',
            'role': 'end_user'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'testuser')
        # Ensure password is not returned in response
        self.assertNotIn('password', response.data)

    def test_login_user(self):
        """
        Ensure a registered user can log in and get a token.
        """
        # First, create a user to log in with
        CustomUser.objects.create_user(
            username='testuser',
            password='somepassword123'
        )

        url = reverse('login')
        data = {'username': 'testuser', 'password': 'somepassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_user_wrong_credentials(self):
        """
        Ensure login fails with wrong credentials.
        """
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_login_user_generates_new_token(self):
        """
        Ensure that logging in multiple times invalidates the old token
        and provides a new one.
        """
        user = CustomUser.objects.create_user(
            username='testuser',
            password='somepassword123'
        )
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'somepassword123'}

        # First login
        response1 = self.client.post(url, data, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        token1 = response1.data['token']

        # Second login
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        token2 = response2.data['token']

        # The tokens should be different, and the old one should be invalid.
        self.assertNotEqual(token1, token2)
        self.assertFalse(Token.objects.filter(key=token1).exists())
        self.assertTrue(Token.objects.filter(key=token2).exists())
