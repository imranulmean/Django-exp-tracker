from django.urls import path

from users.views import GoogleLogin

urlpatterns = [
    path('google', GoogleLogin.as_view(), name='google-login'),
]
