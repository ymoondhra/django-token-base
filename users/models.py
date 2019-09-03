from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add your fields here
    # example: name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username

