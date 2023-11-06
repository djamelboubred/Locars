# Generated by Django 4.2.6 on 2023-11-06 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_user_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='profilePicture',
            field=models.ImageField(default='profile_picture/default_images/profile_default.jpg', upload_to='profile_picture/'),
        ),
    ]
