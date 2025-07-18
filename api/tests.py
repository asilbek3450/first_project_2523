from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Genre, Book
from datetime import date
from decimal import Decimal

class AuthorTests(APITestCase):
    def setUp(self):
        self.author_data = {"name": "Leo Tolstoy", "birth_date": "1828-09-09"}
        self.author = Author.objects.create(**self.author_data)

    def test_create_author(self):
        url = reverse('authors')
        data = {"name": "Abduqahhor", "birth_date": "1821-11-11"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_author(self):
        url = reverse('authors', args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.author.name)

    def test_update_author(self):
        url = reverse('authors', args=[self.author.id])
        data = {"name": "Abduqahhorjon", "birth_date": "1828-09-09"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Leo Nikolayevich Tolstoy")

    def test_delete_author(self):
        url = reverse('authors', args=[self.author.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

