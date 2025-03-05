from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import  LoginUser

urlpatterns = [
    # path('google', GoogleLogin.as_view(), name='google-login'),
    path('login', TokenObtainPairView.as_view(), name="login-user"),
    path('getUser', LoginUser.as_view(), name="login-user")
]
