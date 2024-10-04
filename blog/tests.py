from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class BlogPostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {
                                refresh.access_token}')

    def test_create_blog_post(self):
        response = self.client.post(
            '/api/blogs/', {'title': 'Test', 'content': 'Test content'})
        self.assertEqual(response.status_code, 201)
