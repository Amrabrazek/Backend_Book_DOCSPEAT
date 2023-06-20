from django.test import TestCase
from .models import User, Author, Reader, Reader_books, Book, Page
# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='amr', last_name='abdelrazek', email='amr.3brazek@gmail.com', username='amrabrazek', password='123')

    def test_username_content(self):
        user = User.objects.get(id=1)
        expected_username = f'{user.username}'
        self.assertEqual(expected_username, 'amrabrazek')

    def test_email_content(self):
        user = User.objects.get(id=1)
        expected_email = f'{user.email}'
        self.assertEqual(expected_email, 'amr.3brazek@gmail.com')