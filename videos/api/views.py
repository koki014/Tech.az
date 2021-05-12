# from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
# from .serializers import *
# from ..models import *

# class VideoViewSet(ModelViewSet):
#     permission_classes = [permissions.AllowAny,]
#     queryset = Video.objects.filter(is_published=True)
#     serializers = {
#         'list': VideoSerializers,
#         'default': VideoCreateSerializers
#     }
    
#     def get_serializer_class(self):
#         return self.serializers.get(self.action, self.serializers.get('default'))