from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models import Articles
from .serializers import ArticleSerializers, ArticleCreateSerializers



class ArticleViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Articles.objects.all()

    serializers = {
        'list': ArticleSerializers,
        'retrieve': ArticleSerializers,
        'default': ArticleCreateSerializers
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers.get('default'))

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset