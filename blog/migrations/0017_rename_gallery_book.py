# Generated by Django 5.0.6 on 2024-05-22 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_gallery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Book',
        ),
    ]