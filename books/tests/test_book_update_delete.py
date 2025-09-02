from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BookUpdateDeleteTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.u1 = User.objects.create_user(
            "reuben", "reubenabrahams77@gmail.com", "testpass123"
        )
        self.u2 = User.objects.create_user("other", "other@example.com", "testpass123")

        self.b1 = Book.objects.create(title="Old Title", author="A", owner=self.u1)
        self.b2 = Book.objects.create(
            title="Other User Book", author="B", owner=self.u2
        )

        self.url_update_u1 = reverse("book_update", args=[self.b1.pk])
        self.url_delete_u1 = reverse("book_delete", args=[self.b1.pk])
        self.url_update_u2 = reverse("book_update", args=[self.b2.pk])
        self.url_delete_u2 = reverse("book_delete", args=[self.b2.pk])
        self.url_list = reverse("book_list")

    def test_update_requires_login(self):
        resp = self.client.get(self.url_update_u1)
        self.assertEqual(resp.status_code, 302)  # redirect to login

    def test_delete_requires_login(self):
        resp = self.client.get(self.url_delete_u1)
        self.assertEqual(resp.status_code, 302)

    def test_user_cannot_edit_others_book(self):
        self.client.login(username="reuben", password="testpass123")
        resp = self.client.post(
            self.url_update_u2, {"title": "Mercy", "author": "David Baldacci"}
        )
        self.assertEqual(resp.status_code, 404)
        self.b2.refresh_from_db()
        self.assertEqual(self.b2.title, "Other User Book")

    def test_user_cannot_delete_others_book(self):
        self.client.login(username="reuben", password="testpass123")
        resp = self.client.post(
            self.url_delete_u2,
        )
        self.assertEqual(resp.status_code, 404)
        self.assertTrue(Book.objects.filter(pk=self.b2.pk).exists())

    def test_user_can_update_own_book(self):
        self.client.login(username="reuben", password="testpass123")
        resp = self.client.post(
            self.url_update_u1, {"title": "New Title", "author": "A"}
        )
        self.assertEqual(resp.status_code, 302)  # redirect to listt
        self.b1.refresh_from_db()
        self.assertEqual(self.b1.title, "New Title")

    def test_user_can_delete_own_book(self):
        self.client.login(username="reuben", password="testpass123")
        resp = self.client.post(
            self.url_delete_u1,
        )
        self.assertEqual(resp.status_code, 302)  # redirect to list
        self.assertFalse(Book.objects.filter(pk=self.b1.pk).exists())
