from .views import UserViewSet, UserCreateViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'register', UserCreateViewSet, basename='users')

urlpatterns = [
    
]


urlpatterns += router.urls