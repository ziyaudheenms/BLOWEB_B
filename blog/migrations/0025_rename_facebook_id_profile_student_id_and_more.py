# Generated by Django 5.0.6 on 2024-07-17 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_rename_profession_blog_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='facebook_id',
            new_name='student_Id',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='instragram_id',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='about_you',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitter_id',
        ),
    ]
