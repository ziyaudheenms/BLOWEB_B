# Generated by Django 5.0.6 on 2024-05-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_profile_avatar_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]