from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPIView, LoginAPI, ProfileAPIView, UserReadOnlyModelViewSets



urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('profile/', ProfileAPIView.as_view(), name='user_profile'),
    path('profile/<int:user_id>/articles/', UserReadOnlyModelViewSets.as_view({'get': 'get_users_news'}), name='get_news'),

]

