from rest_framework.serializers import ModelSerializer
from blog.models import Blog,Category,Like,Profile ,Comment
from rest_framework import serializers
from django.contrib.auth.models import User
class BlogSerializer(ModelSerializer):
    username = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    like_Count = serializers.SerializerMethodField()
    avatar_img = serializers.SerializerMethodField()
    class Meta:
        fields = ('id' ,'username','category','cover_img','title','short_discription','like_Count','avatar_img' , 'detail_discription')
        model =  Blog

    def get_username(self,instance):
        return instance.username.username
    
    def get_category(self,instance):

        return instance.category.title
    
    def get_like_Count(self,instance):
        like = Like.objects.filter(blog = instance.id)
        like_count = len(like)
        return like_count
    def get_avatar_img(self,instance):
        IMG = Profile.objects.get(username = instance.username)
        path = str(IMG.avatar_img)
        return f"http://localhost:8000/media/{path}"
   
    

class CategorySerializer(ModelSerializer):
    class Meta:
        fields = ('id' , 'title')
        model = Category

class SinglePageSerializer(ModelSerializer):
    username = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    like_Count = serializers.SerializerMethodField()
    Department = serializers.SerializerMethodField()
    avatar_img = serializers.SerializerMethodField()
    class Meta:
        fields = ('id' ,'username','category','cover_img','title','short_discription','like_Count','detail_discription','Department','avatar_img')
        model =  Blog

    def get_username(self,instance):
        return instance.username.username
    
    def get_category(self,instance):
        return instance.category.title
    
    def get_like_Count(self,instance):
        like = Like.objects.filter(blog = instance.id)
        like_count = len(like)
        return like_count
    def get_Department(self,instance):
        pro_fession = Profile.objects.get(username = instance.username)
        return pro_fession.Department
    def get_avatar_img(self,instance):
        IMG = Profile.objects.get(username = instance.username)
        path = str(IMG.avatar_img)
        return f"http://localhost:8000/media/{path}"
    
class UserProfileSerializer(ModelSerializer):
    username = serializers.SerializerMethodField()
    total_posts = serializers.SerializerMethodField()
    Gmail_id = serializers.SerializerMethodField()
    Likes_given = serializers.SerializerMethodField()
    comments_written = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = Profile

    def get_username(self,instance):
        return instance.username.username
    def get_comments_written(self,instance):
        Total = Comment.objects.filter(username = instance.username)
        number = len(Total)
        return number
    def get_total_posts(self,instance):
        Total = Blog.objects.filter(username = instance.username)
        number = len(Total)
        return number
    def get_Gmail_id(self,instance):
        ID = User.objects.get(username = instance.username)
        return ID.email
    
    def get_Likes_given(self,instance):
        UserLikes = Like.objects.filter(username = instance.username)
        number = len(UserLikes)
        return number
    
class AllprofileSerializer(ModelSerializer):
    username = serializers.SerializerMethodField()
    total_posts = serializers.SerializerMethodField()
    Gmail_id = serializers.SerializerMethodField()
    Likes_given = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Profile

    def get_username(self,instance):
        return instance.username.username
    def get_total_posts(self,instance):
        Total = Blog.objects.filter(username = instance.username)
        number = len(Total)
        return number
    def get_Gmail_id(self,instance):
        ID = User.objects.get(username = instance.username)
        return ID.email
   
    def get_Likes_given(self,instance):
        UserLikes = Like.objects.filter(username = instance.username)
        number = len(UserLikes)
        return number

        return number
class CommentSerializer(ModelSerializer):
    username = serializers.SerializerMethodField()
    avatar_img = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = Comment

    def get_username(self , instance):
        return instance.username.username
    def get_avatar_img(self , instance):
        if Profile.objects.filter(username = instance.username).exists():
            IMG = Profile.objects.get(username = instance.username)
            path = str(IMG.avatar_img)
            return f"http://localhost:8000/media/{path}"
        else:
            return f"http://localhost:8000/media/blog/AvatarImg/business.png"
   
    

class UserSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
