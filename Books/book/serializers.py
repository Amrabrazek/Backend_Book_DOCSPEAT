from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Reader_books, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("__all__")

class ReaderbookSerializer(serializers.ModelSerializer):
    reader = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    class Meta:
        model = Reader_books
        fields = "__all__"