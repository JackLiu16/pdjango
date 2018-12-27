# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from api.models import Book
from rest_framework import viewsets
from django.views.generic import View
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from api.serializers import UserSerializer, GroupSerializer,BookSerializer
# ViewSets define the view behavior.
class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Test(View):
    def get(self,request):
        return HttpResponse("TEST")