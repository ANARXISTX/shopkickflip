# Generated by Django 5.0.4 on 2024-11-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_basket_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='selected_size',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
