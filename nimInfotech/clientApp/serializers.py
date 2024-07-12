from rest_framework import serializers
from clientApp.models import *

class clientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=client
        fields='__all__'
class projectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=project
        fields='__all__'
class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=user
        fields='__all__'
