from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
import json
from datetime import datetime

# Just a simple way see if the server is running.
@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'Server is live. Current time is'
    return Response(data = message + date, status = status.HTTP_200_OK)

# Registration system
@api_view(['POST'])
def registerUser(request, *args, **kwargs):

    payload=json.loads(json.dumps(request.POST))
    email           = payload["email"]
    username        = payload["username"]
    password        = payload["password"]
    phone           = payload["phone"]
    first_name      = payload["firstname"]
    last_name       = payload["lastname"]
    messages        = []

    try:
        #Checking if the username is not already taken
        user = get_user_model().objects.get(username = username)
        messages.append("The username you entered has already been taken.")
        response = json.dumps([{ 'messages' : messages}])
        return Response(response, status= status.HTTP_200_OK)

    except get_user_model().DoesNotExist:
        #Registering the user
        user = get_user_model().objects.create_user(
                                        username        = username,
                                        email           = email,
                                        password        = password,
                                        first_name      = first_name,
                                        last_name       = last_name,
                                        phone           = phone)
        user.save()
        messages.append("Account created.")
        response = json.dumps([{ 'messages' : messages}])
        return Response(response, status= status.HTTP_200_OK)

# Login system
'''
the login system is pre-built in Djoser framework which is currently installed in this project. we don't have to re-write that. 
'''

