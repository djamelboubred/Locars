from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser,BaseUserManager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
#from .managers import UserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail est obligatoire.')
        if not username:
            raise ValueError('Le nom d\'utilisateur est obligatoire.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')

        return self.create_user(username,email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    profilePicture = models.ImageField(upload_to='profile_picture/',
                                default='profile_picture/default_images/profile_default.jpg')
    locarist = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)

    def get_creation_month_year(self):
        return self.date_creation.strftime('%b %Y')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Car(models.Model):
    
    FUEL_CHOICES = (
        ('A', 'Essence'),
        ('B', 'Diesel'),
        ('C', 'Électrique'),
    )

    marque = models.CharField(max_length=50, default='')
    model = models.CharField(max_length=50, default='')
    year = models.PositiveIntegerField()

    fuel = models.CharField(max_length=1, choices=FUEL_CHOICES)
    def __str__(self):
        return self.name

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
