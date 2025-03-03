from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ["id", "username", "email", "password", "displayName", "profilePicture", "isAdmin"]
        extra_kwargs = {"password": {"write_only": True}}