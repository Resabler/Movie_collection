from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import Registerationserializer,Movieserializer,Collectionserializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
from .models import Movie,Collection
from rest_framework import serializers

# Create your views here.
class Registerationview(APIView):
      def post(self, request):
        serializer=Registerationserializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)

            # The access token is used for authentication, you can return it here
            access_token = str(refresh.access_token)
            return JsonResponse({"message":"User created successfully","token":access_token})
        else:
            return JsonResponse({"error":"An error has been occurred"},status=400)
        
class Movielistcreateview(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=Movieserializer
    permission_classes=[IsAuthenticated]


class Moviedestroyupdateview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=Movieserializer
    permission_classes=[IsAuthenticated]

class Collectionlistcreateview(generics.ListCreateAPIView):
    queryset=Collection.objects.all()
    serializer_class=Collectionserializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        # Check if the username exists before creating the collection
        user_username = self.request.data.get('user_username')
        if not User.objects.filter(username=user_username).exists():
            raise serializers.ValidationError(f"User with username {user_username} does not exist.")
        serializer.save()

class Collectiondestroyupdateview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Collection.objects.all()
    serializer_class=Collectionserializer
    permission_classes=[IsAuthenticated] 
  
   
