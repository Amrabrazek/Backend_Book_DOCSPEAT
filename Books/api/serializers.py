from rest_framework import serializers
from django.utils import timezone
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

# class DateField(serializers.DateField):
#     def to_representation(self, value):
#         value = timezone.localtime(value)
#         return super().to_representation(value.date())

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("__all__")

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
    
# class MyModelSerializer(serializers.ModelSerializer):

#     creator = serializers.ReadOnlyField(source='creator.username')
#     creator_id = serializers.ReadOnlyField(source='creator.id')
#     image_url = serializers.ImageField(required=False)

#     class Meta:
#         model = MyModel
#         fields = ['id', 'creator', 'creator_id', 'title', 'description', 'image_url']
