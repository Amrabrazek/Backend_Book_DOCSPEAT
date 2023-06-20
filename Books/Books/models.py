from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


# autho class model
class User(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=60, null=True, blank=True)
    bio = models. TextField()
    birth_date = models.DateField()

    AUTHOR = 'A'
    READER = 'R'
    USER_TYPE_CHOICES = [
        (AUTHOR, 'Author'),
        (READER, 'Reader'),
    ]
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)

    email = models.EmailField(max_length=254, null=False, blank=False)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        # Use make_password to hash the raw password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Use check_password to compare the raw password to the hashed password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

# book class model
class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


# page class model
class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"