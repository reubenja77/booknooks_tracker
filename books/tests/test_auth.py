from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class AuthTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='reuben',
            email='reubenabrahams77@gmail.com',
            password='testpass123',
        )
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.book_list_url = reverse('book_list')

    def test_login_redirects_to_books_list(self):
        resp = self.client.post(self.login_url, {
            username='reuben',
            password='testpass123',
        })
        self.assertRedirects(resp, self.book_list_url)

    def test_logout_redirects_to_login(self):
        self.client.login(username='reuben', password='testpass123')
        resp = self.client.get(self.logout_url)
        self.assertRedirects(resp, reverse('login'))