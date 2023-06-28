from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False)
                
                
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
