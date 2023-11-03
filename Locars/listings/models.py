from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser,BaseUserManager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
#from .managers import UserManager
# Create your models here.

"""class User(AbstractUser):
    HOST = 'HOST'
    CLIENT = 'CLIENT'

    ROLE_CHOICES = (
        (HOST, 'Hôte'),
        (CLIENT, 'Client'),
    )

    profile_photo = models.ImageField(upload_to='default_images/', default='profile_default.jpg')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
"""

"""class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(('adresse mail'), unique=True)
    username = models.CharField(max_length=20, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_no = models.CharField(max_length=10, default='0000000000')
    role = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(2)])
    picture = models.ImageField(upload_to='default_images/',
                                default='profile_default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #objects = UserManager()

    def __str__(self):
        return self.email

"""
"""
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(('adresse mail'), unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_no = models.CharField(max_length=10, default='0000000000')
    role = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(2)])
    picture = models.ImageField(upload_to='default_images/',
                                default='profile_default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #objects = UserManager()
    def get_by_natural_key(self):
        return self.email

    def __str__(self):
        return self.email


"""
