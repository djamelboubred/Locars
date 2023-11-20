# Generated by Django 4.2.6 on 2023-11-20 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('phone_no', models.CharField(blank=True, max_length=15)),
                ('profilePicture', models.ImageField(default='profile_picture/default_images/profile_default.jpg', upload_to='profile_picture/')),
                ('locarist', models.BooleanField(default=False)),
                ('country', models.CharField(blank=True, max_length=42)),
                ('city', models.CharField(blank=True, max_length=58)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_car', models.CharField(max_length=10, unique=True)),
                ('licence_plate', models.CharField(max_length=20, unique=True)),
                ('marque', models.CharField(default='', max_length=50)),
                ('model', models.CharField(default='', max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('km', models.IntegerField(blank=True, default=0)),
                ('country', models.CharField(default='', max_length=42)),
                ('city', models.CharField(default='', max_length=58)),
                ('street', models.CharField(default='', max_length=50)),
                ('fuel', models.CharField(choices=[('A', 'Essence'), ('B', 'Diesel'), ('C', 'Hybride'), ('D', 'Électrique')], default='', max_length=1)),
                ('nb_door', models.IntegerField(blank=True, default=0, null=True)),
                ('geardbox', models.CharField(blank=True, choices=[('B', 'Manuelle'), ('A', 'Automatique')], max_length=1, null=True)),
                ('profilePicture', models.ImageField(default='profile_picture/default_images/cars.png', upload_to='cars_picture/')),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
