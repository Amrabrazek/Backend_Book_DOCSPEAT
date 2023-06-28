
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
    bio = models. TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    usertype = models.CharField(max_length=10, choices=TYPE_CHOICES, null=False, blank=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

