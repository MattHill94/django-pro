# Generated by Django 3.1.7 on 2021-03-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210312_1625'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
