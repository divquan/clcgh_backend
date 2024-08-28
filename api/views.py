from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import json
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def createUser(request):

        body = json.loads(request.body)

        for i in body.keys():
            if body[i] == '':
                return JsonResponse({'message': f'{i} is required!', "status": 400})

        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        phone_number = body['phone_number']
        password = body['password']
        user_type = body['user_type']

      
       
        # create the user
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password, user_type=user_type, username=email)
        user.save()
        
        return JsonResponse({'message': 'User created successfully!', "status": 200})

    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def login(request):
    # This will only be executed if the user is authenticated
    return JsonResponse({"message": f"Hello, {request.user.username}. You are authenticated!"})


@api_view(['POST'])
def login(request):
        body = json.loads(request.body)
        email = body['email']
    