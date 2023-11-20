# Generated by Django 4.2.6 on 2023-11-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_car_geardbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='geardbox',
            field=models.CharField(blank=True, choices=[('B', 'Manuelle'), ('A', 'Automatique')], max_length=1, null=True),
        ),
    ]
