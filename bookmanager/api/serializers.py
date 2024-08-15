from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    isbn = serializers.CharField(required=True,max_length=13,)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn']

    def validate_isbn(self, value):
        instance = getattr(self, 'instance', None)

        # Allow the current book instance to update without triggering uniqueness validation
        if instance and instance.isbn == value:
            return value

        if Book.objects.filter(isbn=value).exists():
            raise serializers.ValidationError("Book with this ISBN already exists.")

        return value
