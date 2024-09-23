from rest_framework import serializers
from .models import UserDetails

class UserDetailSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=12)
