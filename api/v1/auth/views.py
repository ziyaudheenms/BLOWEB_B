from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
@api_view(['POST'])
def Create(request):
    email = request.data['email']
    username = request.data['username']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    if not User.objects.filter(username = username).exists():
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name = first_name,
            last_name = last_name,
          
        )

        responceData={
            "status_code":5000,
            'message':'successfully created the account'
        }
        return Response(responceData)
    else:
        responceData={
            "status_code":5001,
            'message':'Same Username Exists'
        }
        return Response(responceData)
