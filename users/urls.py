from django.urls import path

from users.views import GoogleLogin, Test

urlpatterns = [
    path('google', GoogleLogin.as_view(), name='google-login'),
    path('test', Test.as_view(), name="test-view")
]
