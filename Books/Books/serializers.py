from rest_framework import serializers
from .models import User, Author,Reader, Reader_books, Book, Page

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = "__all__"

class ReaderbookSerializer(serializers.ModelSerializer):
    reader = ReaderSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    class Meta:
        model = Reader_books
        fields = "__all__"

class PageSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Page
        fields = ['page_number', 'content', 'book']



class UserBookPageSerializer(serializers.Serializer):
    author = UserSerializer()
    book = BookSerializer()
    page = PageSerializer()

    def to_representation(self, instance):
        data = super(UserBookPageSerializer, self).to_representation(instance)
        return {'user': data['user'], 'book': data['book'], 'page': data['page']}