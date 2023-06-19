from django.db import models


# autho class model
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

# book class model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

# page class model
class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"