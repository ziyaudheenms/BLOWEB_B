from pathlib import Path
from rest_framework import status
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from blog.models import Blog , Category , Profile  ,Like ,Comment
from .serializers import BlogSerializer , CategorySerializer , SinglePageSerializer , UserProfileSerializer ,AllprofileSerializer,UserSerializer,CommentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from django.contrib.auth.models import User
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Show(request):
    instance = Blog.objects.filter(is_deleted = False)
    q = request.GET.get('q')
    if q:
        ids = q.split(',')
        instance = instance.filter(category__in = ids)
    context = {
        "request":request
    }
    serializedData = BlogSerializer(instance=instance,many=True,context=context)
    responce_data = {
        'status_code' : 5000,
        "data": serializedData.data
    }
    return Response(responce_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ShowCategory(request):
    instance = Category.objects.all()
    context = {
        'request' : request
    }
    serializedData = CategorySerializer(instance=instance , many= True , context = context )
    responce_data = {
        "status_code" : 5000,
        "data" : serializedData.data
    }
    return Response(responce_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SearchFilter(request):
    instance = Blog.objects.all()
    q= request.GET.get('q')

    if q:
        instance = instance.filter(title__icontains = q )

    context = {
        'request' : request
    }
    serializedData = BlogSerializer(instance=instance , many= True , context = context )
    responce_data = {
        "status_code" : 5000,
        "data" : serializedData.data
    }
    return Response(responce_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def singlePage(request , pk):
    if Blog.objects.filter(pk = pk).exists():
        instance = Blog.objects.get(pk=pk)
        SerializedData = SinglePageSerializer(instance=instance , context = {"request" : request})
        responce_data = {
        "status_code" : 5000,
        "data" : SerializedData.data
        }
        return Response(responce_data)
    else:
        responce_data = {
            "status_code" : 5001,
            "data" : "page not Exists"
        }
        return Response(responce_data)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserProfile(request):
    if Profile.objects.filter(username = request.user).exists():
        instance = Profile.objects.get(username=request.user)
        context = {
            "request" : request
        }
        serialisedData = UserProfileSerializer(instance=instance , context = context)
        responce_data = {
            'status_code': 5000,
            'data':serialisedData.data
        }
        return Response(responce_data)
    else:
        responce_data = {
            'status_code': 5001,
            'data':'Profile not found'
        }
        return Response(responce_data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllProfiles(request ):
    instance = Profile.objects.all()
    context = {
        'request' : request
    }
    serialisedData = AllprofileSerializer(instance=instance ,many=True, context = context)
    responce_Data = {
        'status_code' : 5000,
        "data" : serialisedData.data
    }
    return Response(responce_Data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def RequestedProfile(request,pk ):
    if Profile.objects.filter(pk = pk).exists():
        instance = Profile.objects.get(id = pk)
        context = {
            'request' : request
        }
        serialisedData = AllprofileSerializer(instance=instance , context = context)
        responce_Data = {
            'status_code' : 5000,
            "data" : serialisedData.data
        }
        return Response(responce_Data)
    else:
        responce_Data = {
            'status_code' : 5001,
            "data" : "user Profile does'nt exists"
        }
        return Response(responce_Data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MyProjects(request):
    instance = Blog.objects.filter(username = request.user)
    context = {
        'request' : request
    }
    serializedData = BlogSerializer(instance=instance , many=True, context = context )
    responce_Data = {
            'status_code' : 5000,
            "data" : serializedData.data
        }
    return Response(responce_Data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MoreSuggestions(request):
    q = request.GET.get('q')
    if q:
        instance = Blog.objects.filter(username__username__iexact = q)
        context = {
            'request' : request
        }
        serialisedData = BlogSerializer(instance=instance , many = True ,context = context )
        responce_data = {
            'status_code' : 5000,
            "data" : serialisedData.data
        }
        return Response(responce_data)
    else:
        responce_data = {
            'status_code' : 5001,
            "data" : 'no data provided'
        }
        return Response(responce_data)


   
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BuildProfile(request):
    if not Profile.objects.filter(username = request.user).exists():
        firstName = request.data['FirstName']
        LastName = request.data['LastName']
        Department = request.data['profession']
        aboutYou = request.data['aboutYou']
        facebook = request.data['facebook']
        insta = request.data['insta']
        twitter = request.data['twitter']
        img = request.data['img']
        
        Profile.objects.create(
            username = request.user,
            first_name = firstName,
            last_name = LastName,
            Department = Department,
            about_you = aboutYou,
            avatar_img = img,
            facebook_id = facebook,
            instragram_id = insta,
            twitter_id = twitter,

        )
        responce_data = {
            'status_code' : 5000,
            "data" : "profile created successfully"
        }
        return Response(responce_data)
    else:
        responce_data = {
            'status_code' : 5001,
            "data" : "You have profile"
        }
        return Response(responce_data)




@api_view(['POST'])
@permission_classes([AllowAny])
def BuildProfileUser(request):
   
    firstName = request.data['FirstName']
    LastName = request.data['LastName']
    Department = request.data['Department']
    UserName = request.data['UserName']
    UserNAME  = User.objects.get(username = UserName)
    Year = request.data['Year']
    StudentId = request.data['StudentId']
    email = request.data['Email']
    img = request.data['img']
        
    Profile.objects.create(
        username = UserNAME,
        first_name = firstName,
        last_name = LastName,
        Department = Department,
        avatar_img = img,
        student_id = StudentId,
        year = Year,

    )
    responce_data = {
        'status_code' : 5000,
        "data" : "profile created successfully"
    }
    return Response(responce_data)













@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BuildBlog(request):
    if  Profile.objects.filter(username = request.user).exists():
        Title = request.data['Title']
        short_disc = request.data['short_disc']
        categories = request.data['Category']
        Cover_img = request.data['Cover_img']
        content = request.data['content']
        category_instance = Category.objects.get(id = categories)
        
        Blog.objects.create(
            username = request.user,
            category = category_instance,
            cover_img = Cover_img,
            short_discription = short_disc,
            title = Title,
            detail_discription = content,
        )
        responce_data = {
            'status_code' : 5000,
            "data" : "blog created successfully"
        }
        return Response(responce_data)
    else:
        responce_data = {
            'status_code' : 5001,
            "data" : "You don't have profile"
        }
        return Response(responce_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DeleteBlog(request , pk):
    if Blog.objects.filter(pk = pk).exists():
        instance = Blog.objects.get(pk = pk)
        instance.delete()
        responce_data = {
            "stauts_code" : 5000,
            "Data" : "blog deleted successfully!"
        }
        return Response(responce_data)
    else:
        responce_data = {
            "stauts_code" : 5000,
            "Data" : "blog not found!"
        }
        return Response(responce_data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def BlogLikeUpdate(request , pk):
    if Blog.objects.filter(pk =pk).exists():
        post = Blog.objects.get(pk =pk )
        if Like.objects.filter(blog = post).exists():
            instance = Like.objects.filter(blog = post)
            if instance.filter(username = request.user).exists():
                instance.get(username = request.user).delete()
                responce_data = {
                "status_code" : 5000,
                "data" : "disliked successfully"
                }
                return Response(responce_data)
            else:
                Like.objects.create(
                    username = request.user,
                    blog = post
                )
                responce_data = {
                "status_code" : 5000,
                "data" : "liked successfully"
                }
                return Response(responce_data)
            responce_data = {
                "status_code" : 5000,
                "data" : "Successfully enterde"
            }
            return Response(responce_data)
        else:
            Like.objects.create(
                username = request.user,
                blog = post
            )
            responce_data = {
                "status_code" : 5000,
                "data" : "Successfully liked"
            }
            return Response(responce_data)
    else:
        responce_data = {
            "status_code" : 5001,
            "data" : "Successfully disliked"
        }
        return Response(responce_data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BlogPostUpdate(request , pk):
    if Blog.objects.filter(pk = pk).exists():
        post = Blog.objects.get(pk=pk)
        print(request.data)
        
        serializedData = BlogSerializer(instance=post , data=request.data )
        print(serializedData)
        if serializedData.is_valid():
            print('hoi')
            serializedData.save()
            print('goat')
            responce_data = {
                "status_code" : 5000,
                "message" : 'Blog is not updated',
                
            }
            return Response(responce_data)
        else:
            responce_data = {
                "status_code" : 5000,
                "message" : serializedData.errors
            }
            return Response(responce_data)
    else:
        responce_data = {
            "status_code" : 5000,
            "message" : 'Blog not exists'
        }
        return Response(responce_data)

    




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UserProfileUpdate(request , pk):
    if Profile.objects.filter(pk = pk).exists():
        profile = Profile.objects.get(pk=pk)
        print(request.data)
        serializedData = UserProfileSerializer(instance=profile , data=request.data , partial = True)
        if serializedData.is_valid():
            serializedData.save()
            responce_data = {
                "status_code" : 5000,
                "message" : 'profile is updated'
            }
            return Response(responce_data)
        else:
            responce_data = {
                "status_code" : 5001,
                "message" : serializedData.errors
            }
            return Response(responce_data)
    else:
        responce_data = {
            "status_code" : 5001,
            "message" : 'Profile not found'
        }
        return Response(responce_data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserDetail(request):
    if User.objects.filter(username = request.user).exists():
        instance = User.objects.get(username = request.user)
        context = {
        "request" : request
        }
        serializedData = UserSerializer(instance=instance , context=context)
        responce_data = {
        "status_code" : 5000,
        "data" : serializedData.data,
        "message" : True
        }
        return Response(responce_data)
    else:
        responce_data = {
        "status_code" : 5000,
        "message" : False
        }
        return Response(responce_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PageComment(request , pk):
    if Blog.objects.filter(pk = pk).exists():
        blog = Blog.objects.get(pk = pk)
        instance = Comment.objects.filter(blogPost = blog) 
        context={
        'request' :request
        }
        serializedData = CommentSerializer(instance=instance , many=True ,context = context)
        responce_data = {
            'status_code' : 5000,
            'data' : serializedData.data
        }
        return Response(responce_data)
    else:
        responce_data = {
            'status_code' : 5000,
            'data' : 'blog not found'
        }
        return Response(responce_data)
    

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateComment(request , pk):
    if Profile.objects.filter(username = request.user).exists():

        if Blog.objects.filter(pk = pk).exists():
            text = request.data['text']
            blogInstance = Blog.objects.get(pk = pk )
            Comment.objects.create(
                username = request.user,
                text = text,
                blogPost = blogInstance
            )
            responce_data = {
                "stauts_code" : 5000,
                "Data" : "Comment created successfully!"
            }
            return Response(responce_data)
        else:
            responce_data = {
                "stauts_code" : 5000,
                "Data" : "blog doesn't exists!"
            }
            return Response(responce_data)
    else:
        responce_data = {
            "stauts_code" : 5001,
            "Data" : "profile doesn't exists!"
        }
        return Response(responce_data)

