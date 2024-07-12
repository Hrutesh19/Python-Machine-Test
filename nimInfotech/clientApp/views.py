from django.shortcuts import render
from clientApp.serializers import *
from rest_framework import viewsets
from clientApp.models import *
# Create your views here.

class clientViewset(viewsets.ModelViewSet):
    queryset=client.objects.all()
    serializer_class=clientSerializer

class projectViewset(viewsets.ModelViewSet):
    queryset=project.objects.all()
    serializer_class=projectSerializer

class userUserviewset(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class=userSerializer
