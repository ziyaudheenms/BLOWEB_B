# Generated by Django 5.0.6 on 2024-05-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_avatar_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='avatar_img',
            field=models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Rishabh_Pant_%2829693622367%29_%28cropped%29.jpg/330px-Rishabh_Pant_%2829693622367%29_%28cropped%29.jpg', upload_to='blog/AvatarImg'),
        ),
    ]
