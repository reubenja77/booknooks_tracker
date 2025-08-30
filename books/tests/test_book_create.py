from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from books.models import Book

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
        resp = self.client.get(self.url_create)
        expected = f'{settings.LOGIN_URL}?next={self.url_create}'
        self.assertRedirects(resp, expected, fetch_redirect_response=False)

    def test_valid_post_creates_book_bound_to_user(self):
        self.client.login(username='reuben', password='testpass123')
        payload = {
            'title': 'The Hunt For Red October',
            'author': 'Tom Clancy',
            'description': 'Classic Spy Novel.',
            'date_read': '',
        }
        resp = self.client.post(self.url_create, data=payload)
        self.assertRedirects(resp, self.url_list)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.first()
        self.assertEqual(book.owner, self.user)
        self.assertEqual(book.title, payload['title'])
        self.assertEqual(book.author, payload['author'])
