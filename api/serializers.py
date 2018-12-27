from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ( 'name',)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = (
            'id',
            'title'
        )
