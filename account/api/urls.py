from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPIView, LoginAPI, ProfileAPIView



urlpatterns = [
    path('accounts/register/', RegisterAPIView.as_view(), name='register'),
    path('accounts/login/', LoginAPI.as_view(), name='login'),
    path('accounts/password-reset/', include('django_rest_resetpassword.urls', namespace='password_reset')),
    path('accounts/user-profile/', ProfileAPIView.as_view(), name='user_profile'),
]

