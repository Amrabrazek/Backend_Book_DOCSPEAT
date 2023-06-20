from django.contrib import admin

# Register your models here.
from .models import User, Author,Reader, Reader_books, Book, Page

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Reader_books)
admin.site.register(Book)
admin.site.register(Page)