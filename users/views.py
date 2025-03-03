from random import choice
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import AccessToken

class GoogleLogin(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        displayName = data.get('displayName')
        profilePicture = data.get('googlePhotoUrl')

        # Check if all required fields are present
        if not email or not displayName or not profilePicture:
            return Response({"error": "Missing Fields"}, status=400)

        try:
            # Create the user if they don't exist
            user, created = CustomUser.objects.get_or_create(
                email=email,
                defaults={                    
                    'password': make_password(self.generate_random_password()),  # Generating a random password
                    'displayName': displayName,
                    'profilePicture': profilePicture,
                    'isAdmin': False
                }
            )

            # if not created:
            #     # If the user already exists, return their data
            #     return Response({"message": "User already exists", "data": UserSerializer(user).data}, status=200)

            # # If the user is newly created, return their data
            # return Response(UserSerializer(user).data, status=201)
            # Generate only Access Token
            access_token = str(AccessToken.for_user(user))  # Direct access token

            response_data = {
                "message": "User logged in successfully",
                "user": UserSerializer(user).data,
                "token": access_token  # Sending only access token
            }            
            return Response(response_data, status=200)
            
        except Exception as e:
            # Handle any exceptions and return the error message
            return Response({"error": str(e)}, status=500)

    def generate_random_password(self, length=16):
        """Generates a random password"""
        characters = string.ascii_letters + string.digits
        return ''.join(choice(characters) for _ in range(length))