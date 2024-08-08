# Generated by Django 5.0.6 on 2024-05-15 15:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('about_you', models.TextField()),
                ('avatar_img', models.ImageField(default='https://th.bing.com/th/id/OIP.CsCEiIgcxJ54PXFJ-Ep5nQHaHa?w=216&h=216&c=7&r=0&o=5&dpr=1.3&pid=1.7', upload_to='blog/AvatarImg')),
                ('facebook_id', models.CharField(blank=True, max_length=50, null=True)),
                ('instragram_id', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=50, null=True)),
                ('total_posts', models.IntegerField(default=0)),
                ('bloweb_rating', models.FloatField(default=0)),
                ('bloweb_member', models.DateField(auto_now_add=True)),
                ('total_likes', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]