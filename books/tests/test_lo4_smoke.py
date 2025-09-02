from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from books.models import Book


class LO4SmokeTests(TestCase):
    """
    Minimal, end-to-end style checks:
    - signup -> auto-login -> redirect
    - login -> redirect
    - book create requires login
    - valid POST creates Book bound to the user
    - list shows only current user's books
    """

    def setUp(self):
        self.User = get_user_model()
        # Common URLs
        self.url_index = reverse("index")
        self.url_login = reverse("login")
        self.url_signup = reverse("signup")
        self.url_list = reverse("book_list")
        self.url_create = reverse("book_create")

    def test_index_renders(self):
        resp = self.client.get(self.url_index)
        self.assertEqual(resp.status_code, 200)

    def test_signup_creates_user_and_logs_in(self):
        payload = {
            "username": "alice",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        }
        resp = self.client.post(self.url_signup, payload, follow=True)
        # Should land on book list after auto-login
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context["user"].is_authenticated)

    def test_login_redirects_to_book_list(self):
        self.User.objects.create_user(
            username="bob", email="bob@example.com", password="Testpass123"
        )
        resp = self.client.post(
            self.url_login, {"username": "bob", "password": "Testpass123"}, follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context["user"].is_authenticated)

    def test_book_create_requires_login(self):
        resp = self.client.get(self.url_create)
        # not logged in -> redirect to login
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse("login"), resp["Location"])

    def test_valid_post_creates_book_bound_to_user_and_lists(self):
        user = self.User.objects.create_user(
            username="reuben", email="reuben@example.com", password="Testpass123"
        )
        self.client.login(username="reuben", password="Testpass123")

        payload = {
            "title": "The Hunt for Red October",
            "author": "Tom Clancy",
            "description": "Classic techno-thriller.",
            "date_read": "",  # optional
        }
        resp = self.client.post(self.url_create, data=payload, follow=True)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.first()
        self.assertEqual(book.owner, user)
        self.assertEqual(book.title, payload["title"])

        # list shows only current user's books
        list_resp = self.client.get(self.url_list)
        self.assertContains(list_resp, "The Hunt for Red October")
