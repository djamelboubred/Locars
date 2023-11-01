from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    HOST = 'HOST'
    CLIENT = 'CLIENT'

    ROLE_CHOICES = (
        (HOST, 'Hôte'),
        (CLIENT, 'Client'),
    )

    profile_photo = models.ImageField(upload_to='default_images/', default='profile_default.jpg')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)