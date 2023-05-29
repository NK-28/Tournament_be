from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    CHOICES = (
        (USER, 'user'),
        (ADMIN, 'admin'),)

    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(
        'Role',
        max_length=16,
        null=False,
        default=USER,
        choices=CHOICES,
    )

