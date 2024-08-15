from django.test import TestCase
from rest_framework.exceptions import NotFound
from api.services import BookService
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book

class BookServiceTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123'
        )
        self.request = None  # Mock or setup request data as needed

    def test_list_books(self):
        service = BookService(self.request)
        books = service.list_books()
        self.assertEqual(books.count(), 1)

    def test_create_book(self):
        self.request.data = {
            'title': 'New Book',
            'author': 'New Author',
            'isbn': '9876543210987'
        }
        service = BookService(self.request)
        book = service.create_book()
        self.assertEqual(book.title, 'New Book')
        self.assertEqual(book.isbn, '9876543210987')

    def test_create_book_with_existing_isbn(self):
        self.request.data = {
            'title': 'Another Book',
            'author': 'Another Author',
            'isbn': '1234567890123'
        }
        service = BookService(self.request)
        with self.assertRaises(Exception) as context:
            service.create_book()
        self.assertEqual(str(context.exception), 'Book with the provided ISBN already exists')

    def test_update_book(self):
        self.request.data = {
            'title': 'Updated Book',
            'isbn': '1234567890124'
        }
        service = BookService(self.request)
        book = service.update_book(self.book.id)
        self.assertEqual(book.title, 'Updated Book')
        self.assertEqual(book.isbn, '1234567890124')

    def test_update_book_with_existing_isbn(self):
        Book.objects.create(
            title='Another Book',
            author='Another Author',
            isbn='1234567890125'
        )
        self.request.data = {
            'isbn': '1234567890125'
        }
        service = BookService(self.request)
        with self.assertRaises(Exception) as context:
            service.update_book(self.book.id)
        self.assertEqual(str(context.exception), 'Book with this ISBN already exists')

    def test_delete_book(self):
        service = BookService(self.request)
        service.delete_book(self.book.id)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_retrieve_book_not_found(self):
        service = BookService(self.request)
        with self.assertRaises(NotFound) as context:
            service.retrieve_book(9999)
        self.assertEqual(str(context.exception), 'Book not found')




class BookAPITestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123'
        )
        self.list_create_url = reverse('book-list-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})

    def test_list_books(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertGreater(len(response.data['data']), 0)

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'isbn': '9876543210987'
        }
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['title'], 'New Book')

    def test_create_book_with_existing_isbn(self):
        data = {
            'title': 'Another Book',
            'author': 'Another Author',
            'isbn': '1234567890123'
        }
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertEqual(response.data['message'], 'Book with the provided ISBN already exists')

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['title'], 'Test Book')

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'isbn': '1234567890124'
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data']['title'], 'Updated Book')

    def test_update_book_with_existing_isbn(self):
        Book.objects.create(
            title='Another Book',
            author='Another Author',
            isbn='1234567890125'
        )
        data = {
            'isbn': '1234567890125'
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertEqual(response.data['message'], 'Book with this ISBN already exists')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['message'], 'Book deleted successfully')

    def test_delete_book_not_found(self):
        invalid_url = reverse('book-detail', kwargs={'pk': 9999})
        response = self.client.delete(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data['success'])
        self.assertEqual(response.data['message'], 'Book not found')
