from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from .models import Book

# Create your tests here.
class BookCreateViewTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='reuben',
            email='reubenabrahams77@gmail.com',
            password='testpass123',
        )
        self.url_create = reverse('book_create')
        self.url_list = reverse('book_list')

def test_create_requires_login(self):
    response = self.client.get(self.url_create)
    expected_redirect = f'{settings.LOGIN_URL}?next={self.url_create}'
    self.assertRedirects(response, expected_redirect, fetch_redirect_response=False)

    response_post = self.client.post(self.url_create, {
        'title': 'Trust',
        'author': 'Hernan Diaz',
    })
    self.assertRedirects(response, expected_redirect, fetch_redirect_response=False)
    self.assertEqual(Book.objects.count(), 0)

def test_valid_post_creates_book_bound_to_user(self):
    logged_in = self.client.login(username='reuben', password='testpass123')
    self.assertTrue(logged_in)

    payload = {
        'title': 'The Hunt For Red October',
        'author': 'Tom Clancy',
        'description': 'Classic Spy Novel.',
        'date_read': '',
    }
    response = self.client.post(self.url_create, data=payload)

    self.assertRedirects(response, self.url_list)
    self.assertEqual(Book.objects.count(), 1)
    book = Book.objects.first()
    self.assertEqual(book.owner, self.user)