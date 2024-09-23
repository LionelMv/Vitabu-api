from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from oauth2_provider.models import AccessToken
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class OIDCTestCase(TestCase):

    def setUp(self):
        """Setup to create sample data"""
        self.client = APIClient()
        self.protected_url = reverse('customer-list')

    def test_google_login_url(self):
        """Test that the Google OIDC login URL is reachable"""
        url = reverse('account_login')  # Django-allauth's login URL
        response = self.client.get(url)
        # print(response.content) # debugging

        # Ensure the login page loads
        self.assertEqual(response.status_code, 200)
        # Ensure the page contains Google login option
        self.assertContains(response, "Google")

    # def test_google_oidc_redirect(self):
    #     """Test that the user is redirected to Google for OIDC login"""
    #     # Get the Google login URL
    #     google_login_url = reverse('accounts/google/login/callback/')
    #     response = self.client.get(google_login_url)
    #     # Ensure redirection to Google
    #     self.assertEqual(response.status_code, 302)
    #     # Ensure the redirect is to Google's login page
    #     self.assertIn('accounts.google.com', response.url)

    def test_protected_view_requires_authentication(self):
        """Test that an unauthenticated user cannot access the API"""
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_access(self):
        """Test that an authenticated user can access the API"""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        # Create an OAuth2 token for the user
        self.token = AccessToken.objects.create(
            user=self.user,
            token='testtoken123',  # Mock token
            expires=timezone.now() + timedelta(hours=1)  # token expiration
        )

        # Add the token to the client for authenticated requests
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token.token)
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
