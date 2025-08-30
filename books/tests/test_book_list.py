from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from books.models import Book

# Create your tests here.
class BookListViewTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.u1 = self.User.objects.create_user(
            username='reuben',
            email='reubenabrahams77@gmail.com',
            password='testpass123',
        )
        self.u2 = self.User.objects.create_user(
            username='other',
            email='other@example.com',
            password='testpass123',
        )

        # Book for u1
        self.b1 = Book.objects.create(
            title='Black Ops', author='Stephen Leather', owner=self.u1
        )
        self.b2 = Book.objects.create(
            title='Tripwire', author='Lee Childs', owner=self.u1
        )

        # Book for u2 (should not be visible to ul)
        self.b3 = Book.objects.create(
            title='Red Strike', author='Chris Ryan', owner=self.u2
        )

        self.url_list = reverse('book_list')

    def test_list_requires_login(self):
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 302)   # redirect to login

    def test_shows_only_current_users_books(self):
        self.client.login(username='reuben', password='testpass123')
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)

        # Should see u1's books...
        self.assertContains(resp, 'Black Ops')
        self.assertContains(resp, 'Tripwire')

        # ...NOT see u2's book
        self.assertNotContains(resp, 'Red Strike')

    def test_search_q_filters_results(self):
        self.client.login(username='reuben', password='testpass123')
        # search for 'Black'
        resp = self.client.get(self.url_list, {'q': 'Black'})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Black Ops')
        self.assertNotContains(resp, 'Tripwire')