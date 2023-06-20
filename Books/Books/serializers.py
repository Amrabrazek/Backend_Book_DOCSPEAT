from rest_framework import serializers
from .models import User, Book, Page

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

class PageSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Page
        fields = ['page_number', 'content', 'book']

class AuthorBookPageSerializer(serializers.Serializer):
    author = UserSerializer()
    book = BookSerializer()
    page = PageSerializer()

    def to_representation(self, instance):
        data = super(AuthorBookPageSerializer, self).to_representation(instance)
        return {'author': data['author'], 'book': data['book'], 'page': data['page']}