from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)


    def __str__(self):
        return self.title


class Blog(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE)
    category=models.ForeignKey(Category , on_delete=models.CASCADE)
    cover_img = models.ImageField(upload_to='images/' ,default='business.png')
    title = models.CharField(max_length=200)
    short_discription = models.CharField(max_length=200)
    detail_discription = models.TextField()
    like_Count = models.IntegerField(default=0)
    is_draft = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    avatar_img = models.ImageField(upload_to='blog/AvatarImg' , default='biology.jpg')
    Department = models.CharField(max_length=200 , default='Cricketer')

    def __str__(self):
        return self.title
    

class Like(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE)
    
class Profile(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    avatar_img = models.ImageField(upload_to='images/' ,default='business.png')
    Gmail_id = models.CharField(max_length=200 , blank=True , null=True)
    student_id = models.CharField(max_length=200 , blank=True , null=True)
    year = models.CharField(max_length=200 ,  blank=True , null=True)
    total_posts = models.IntegerField(default=0)
    bloweb_rating = models.FloatField(default=0)
    bloweb_member = models.DateField(auto_now_add=True)
    total_likes = models.IntegerField(default=0)
    comments_written = models.IntegerField(default=0)
    Likes_given = models.IntegerField(default=0)
    about_you = models.TextField(default="i am a blogger")

    def __str__(self) :
        return self.first_name


class Comment(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE)
    blogPost = models.ForeignKey(Blog , on_delete=models.CASCADE)
    avatar_img = models.ImageField(upload_to='blog/AvatarImg' , default='business.png')
    date = models.DateField(auto_now_add=True)
    text = models.TextField()

    def __str__(self) :
        return self.text

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Book(models.Model):
    title = models.CharField(max_length=100)
    pic = models.ImageField(upload_to=upload_to)
    def __str__(self):
        return self.title
   

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title