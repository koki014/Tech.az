from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()

router.register(r'videos', VideoViewSet)