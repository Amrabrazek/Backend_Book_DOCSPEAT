from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Reader_books, Book, CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("__all__")


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

class ReaderbookSerializer(serializers.ModelSerializer):
    reader = ReaderSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    class Meta:
        model = Reader_books
        fields = "__all__"