from django.urls import path, include
from main.api.views import JoinAPIView, TagViewsSet
from .routers import router


urlpatterns = [
    path('join/', JoinAPIView.as_view(), name='join'),

 
]
urlpatterns += router.urls