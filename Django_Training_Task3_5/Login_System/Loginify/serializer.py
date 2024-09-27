from rest_framework import serializers
from . models import UserDetails



class UserDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model= UserDetails
        fields=['username', 'email', 'password']