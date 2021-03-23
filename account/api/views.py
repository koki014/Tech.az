from rest_framework import viewsets
from django.contrib.auth import get_user_model
from account.models import User
from .serializers import UserSerializer
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Aritcle instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()