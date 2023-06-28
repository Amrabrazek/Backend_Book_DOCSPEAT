from rest_framework import serializers
from book.serializers import BookSerializer
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Page
        fields = ['page_number', 'content', 'book']
