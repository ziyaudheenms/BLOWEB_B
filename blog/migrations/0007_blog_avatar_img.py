# Generated by Django 5.0.6 on 2024-05-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile_avatar_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='avatar_img',
            field=models.ImageField(default='https://th.bing.com/th/id/OIP.CsCEiIgcxJ54PXFJ-Ep5nQHaHa?w=216&h=216&c=7&r=0&o=5&dpr=1.3&pid=1.7', upload_to='blog/AvatarImg'),
        ),
    ]
