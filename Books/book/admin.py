from django.contrib import admin
from .models import Book, Reader_books
# Register your models here.
admin.site.register(Book)
admin.site.register(Reader_books)