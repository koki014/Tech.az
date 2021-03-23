from django.urls import path, include
from main.api.views import JoinAPIView



urlpatterns = [
    path('join/', JoinAPIView.as_view(), name='join'),

]