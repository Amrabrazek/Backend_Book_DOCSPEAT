from django.db import models
from django.utils import timezone
from users.models import CustomUser
from book.models import Book



class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_pages')
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"
    
    def save(self, *args, **kwargs):
        if not self.page_number:
            self.page_number = self.book.book_pages.count() + 1
        super().save(*args, **kwargs)