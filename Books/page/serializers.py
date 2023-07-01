from rest_framework import serializers
from book.serializers import BookSerializer
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Page
        fields = ['id' , 'page_number', 'content', 'book']

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'page_number', 'content', 'book']
