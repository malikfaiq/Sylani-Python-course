from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from datetime import date
from django.contrib.auth.models import User


class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        # Get token
        response = self.client.post(
            "/books/api/token/", {"username": "testuser", "password": "testpass123"}
        )
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "description": "Test Description",
            "published_date": "2023-01-01",
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_books_unauthorized(self):
        # Remove token
        self.client.credentials()
        response = self.client.get("/books/api/books/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_books(self):
        response = self.client.get("/books/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        new_book_data = {
            "title": "New Book",
            "author": "New Author",
            "description": "New Description",
            "published_date": "2023-02-01",
        }
        response = self.client.post("/books/api/books/", new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_single_book(self):
        response = self.client.get(f"/books/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book_data["title"])

    def test_update_book(self):
        updated_data = {
            "title": "Updated Title",
            "author": self.book_data["author"],
            "description": self.book_data["description"],
            "published_date": self.book_data["published_date"],
        }
        response = self.client.put(
            f"/books/api/books/{self.book.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(f"/books/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
