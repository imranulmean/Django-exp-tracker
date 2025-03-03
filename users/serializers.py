from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "displayName", "profilePicture", "isAdmin"]
        extra_kwargs = {"password": {"write_only": True}}