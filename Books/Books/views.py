from django.http import JsonResponse
from django.shortcuts import render
from models import User
from serializers import UserSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def User_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializeredUsers = UserSerializer(users, many=True)
        return Response(serializeredUsers.data)
    if request.method == 'POST':
        serializeredUsers = UserSerializer(data = request.data)
        if serializeredUsers.is_valid():
            serializeredUsers.save()
            return Response(serializeredUsers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializeredUsers.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def User_details(request, id):

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializeredUsers = UserSerializer(user)
        return Response(serializeredUsers.data)
        # return JsonResponse({"Users": serializeredUsers.data} , safe=False)
    elif request.method == 'PUT':
        serializeredUsers = UserSerializer(user, data = request.data)
        if serializeredUsers.is_valid():
            serializeredUsers.save()
            return Response(serializeredUsers.data )
        return Response(serializeredUsers.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
