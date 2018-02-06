from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route

from .models import Users
from .Serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets


class UsersViewSet(viewsets.ModelViewSet):
    base_name = 'users'
    queryset = Users.objects.all()
    serializer_class = UserSerializer
