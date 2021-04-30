from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import *
from ..models import *
from comments.api.serializers import *
from comments.models import *


class VideoViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = Video.objects.filter(is_published=True)
    serializers = VideoSerializers
    
    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset

    def create(self, request):
        serializer = VideoCreateSerializers(data=request, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    @action(detail=False, methods=['GET', 'POST'])
    def comments(self, request, pk):
        video = Video.objects.filter(pk=pk).first()
        self.serializer_class = CommentSerializers
        queryset = Comment.objects.filter(videos=video)
        if video:
            if request.method == 'GET':
                if querset:
                    serializer = CommentSerializers(queryset, many=True, context={'request':request})
                return Response({'message':'comment not founded'})
            else:
                serializer = CommentCreateSerializers(data=request.data, context={'request':request})
                serializer.is_valid(raise_exception=True)
                serializer.save(owner=request.user, videos=video)
                return Response(serializer.data)
        return Response({'message': 'article not founded'}, status=404)

    
    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment_id):
        comment = Comment.objets.filter(pk=comment_id)
        if comment:
            if comment.delete():
                return Response({'message':'Comment deleted'}, status=204)
            else:
                return Response({'message': 'unable to delete comment'}, stautus=400)
        return Response({'message': 'article not founded'}, status=404)
        
