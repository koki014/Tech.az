from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *
from ..models import Comment


class CommentViewsets(ModelViewSet):
    # permission_classes = [IsAuthenticated,]
    queryset = Comment.objects.all()
    permission_classes_by_action = {'create': [IsAuthenticated], 'list': [AllowAny]}

    serializers = {
        'list': CommentSerializers,
        'retrieve': CommentSerializers,
        'default': CommentCreateSerializers,
        'create': CommentCreateSerializers,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers.get('default'))

    def create(self, request, *args, **kwargs):
        return super(CommentViewsets, self).create(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super(CommentViewsets, self).list(request, *args, **kwargs)
    def list(self, request):
        results = CommentSerializers(Comment.objects.all(), many = True)
        return Response(results.data)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]