# Generated by Django 5.0.6 on 2024-07-17 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_blog_cover_img_alter_profile_avatar_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='profession',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profession',
            new_name='department',
        ),
    ]
