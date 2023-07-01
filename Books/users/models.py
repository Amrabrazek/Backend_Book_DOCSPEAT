
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # username = None

    TYPE_CHOICES = [
        ('author', 'Author'),
        ('reader', 'Reader')
    ]

    email = models.EmailField(_("email address"), unique=True)
    title = models.CharField(max_length=60, null=True, blank=True)
    bio = models. TextField(default="A strong author bio establishes your authority, introduces readers to your background, and helps convince them to buy your book. ➡️ An author bio is usually no longer than 100 words, so keep it short and simple. Include your location, relevant experience, and key themes in your work")
    profile_picture = models.ImageField(upload_to='profile_images/', default="profile_images/defaultpp.jpeg")
    usertype = models.CharField(max_length=10, choices=TYPE_CHOICES, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

