from django.db import models
from django.utils import timezone
from users.models import CustomUser



class Book (models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_books', null=False, blank=False) 
    book_cover = models.ImageField(upload_to='book_images/', null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# book pages class model

class Reader_books(models.Model):
    reader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


