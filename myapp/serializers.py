from rest_framework import serializers
from .models import User,Movie,Collection

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('__all__')

class Registerationserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','email')


class Collectionserializer(serializers.ModelSerializer):
    user_username = serializers.CharField(max_length=150)
    class Meta:
        model=Collection
        fields=('__all__')
