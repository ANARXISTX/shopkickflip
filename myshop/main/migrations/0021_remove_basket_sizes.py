# Generated by Django 5.0.1 on 2024-11-16 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_basket_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='sizes',
        ),
    ]
