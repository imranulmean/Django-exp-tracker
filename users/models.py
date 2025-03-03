from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    displayName = models.CharField(max_length=200)
    profilePicture = models.CharField(max_length=500)
    isAdmin = models.BooleanField(default=False)