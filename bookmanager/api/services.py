from rest_framework.exceptions import NotFound, ValidationError
from .models import Book

class BookService:
    def __init__(self, request):
        self.request = request

    def list_books(self):
        return Book.objects.all()

    def create_book(self):
        data = self.request.data
        if Book.objects.filter(isbn=data['isbn']).exists():
            raise ValidationError("Book with the provided ISBN already exists")
        return Book.objects.create(**data)

    def retrieve_book(self, book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound("Book not found")

    def update_book(self, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound("Book does not exist")

        data = self.request.data
        new_isbn = data.get('isbn')

        if new_isbn and new_isbn != book.isbn:
            if Book.objects.filter(isbn=new_isbn).exists():
                raise ValidationError("Book with this ISBN already exists")

        for attr, value in data.items():
            setattr(book, attr, value)

        book.save()
        return book

    def delete_book(self, book_id):
        book = self.retrieve_book(book_id)
        book.delete()
