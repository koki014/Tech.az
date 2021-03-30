from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPIView, LoginAPI, ProfileAPIView



urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('user-profile/', ProfileAPIView.as_view(), name='user_profile'),
]

