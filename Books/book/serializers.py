from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Reader_books, Book, CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'usertype','first_name', 'last_name', 'username', ]

class BookSerializer2(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ("__all__")

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("__all__")


# class BookSerializer(serializers.ModelSerializer):
#     book_cover = serializers.SerializerMethodField()

#     def get_book_cover(self, obj):
#         request = self.context.get('request')
#         if obj.book_cover:
#             return request.build_absolute_uri(obj.book_cover.url)
#         else:
#             return None

#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'summary', 'book_cover', 'publication_date', 'author')



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