# Generated by Django 5.0.6 on 2024-05-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_profile_avatar_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='avatar_img',
            field=models.ImageField(default='business.png', upload_to='blog/AvatarImg'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_img',
            field=models.ImageField(default='business.png', upload_to='blog/AvatarImg'),
        ),
    ]
