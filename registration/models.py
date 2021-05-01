from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Modem


class User(AbstractUser):
    USERNAME_FIELD = 'username'

    ci = models.CharField(max_length=20, verbose_name='CI', unique=True)

    REQUIRED_FIELDS = ['ci', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
