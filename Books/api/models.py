from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from datetime import date
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User as userx

# User class model
class User(models.Model):
    
    # USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=128,null=False, blank=False,)
    
    def set_password(self, raw_password):
        # Use make_password to hash the raw password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Use check_password to compare the raw password to the hashed password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

# Author class model inhariting from the user
class Author(User):
    title = models.CharField(max_length=60, null=True, blank=True)
    bio = models. TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)

# Reader class model inhariting from the user
class Reader(User):
    pass

# Book classs model
class Book (models.Model):

    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, null=True)

    # books of the author in books
    author = models.ForeignKey(userx, on_delete=models.CASCADE, related_name='author_books', null=False, blank=False) 

    book_cover = models.ImageField(upload_to='book_images/', null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# many to many relationship between readers and books 
class Reader_books(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

# book pages class model
class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"
    



def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# class MyModel(models.Model):
#     creator = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="listings")
#     title = models.CharField(
#         max_length=80, blank=False, null=False)
#     description = models.TextField()
#     image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)