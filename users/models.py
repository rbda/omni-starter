from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    grade = models.CharField(max_length=2)
    objects = CustomUserManager()

    def __str__(self):
        return self.username

