from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event, Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['id', 'schoolID', 'firstName', 'lastName']


class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Event
        fields = ['id', 'name', 'time', 'status']

