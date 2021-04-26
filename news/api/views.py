from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from ..models import News

class NewsViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = News.objects.filter(is_published=True)
    serializers = {
        'list': NewsSerializers,
        'default': NewsCreateSerializers
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers.get('default'))


