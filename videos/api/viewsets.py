from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .paginations import LimitPagination
from .serializers import *
from ..models import *
from comments.api.serializers import *
from comments.models import *


class VideoViewSet(ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = Video.objects.filter(is_published=True)    
    serializer_class = VideoSerializers
    lookup_field = 'slug'
    pagination_class = LimitPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset
    

    def retrieve(self, request, slug=None):
        videos = get_object_or_404(Video,slug=slug)
        videos.add_view_count()
        serializer = VideoSerializers(videos)
        return Response(serializer.data)

    # def create(self, request):
    #     serializer = VideoCreateSerializers(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
    #     serializer.save(owner=request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    

    @action(detail=False, methods=['GET', 'POST'])
    def comments(self, request, pk):
        video = Video.objects.filter(pk=pk).first()
        self.serializer_class = CommentSerializers
        queryset = Comment.objects.filter(videos=video)
        if video:
            if request.method == 'GET':
                if queryset:
                    serializer = CommentSerializers(queryset, many=True, context={'request':request})
                return Response({'message':'comment not founded'})
            else:
                print('testtets')
                serializer = CommentCreateSerializers(data=request.data, context={'request':request})
                serializer.is_valid(raise_exception=True)
                serializer.save(owner=request.user, videos=video)
                return Response(serializer.data)
        return Response({'message': 'article not founded'}, status=404)

    
    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment_id):
        comment = Comment.objects.filter(pk=comment_id)
        if comment:
            if comment.delete():
                return Response({'message':'Comment deleted'}, status=204)
            else:
                return Response({'message': 'unable to delete comment'}, stautus=400)
        return Response({'message': 'article not founded'}, status=404)
    
    @action(detail=False, methods=['GET', 'POST'])
    def reply_comment(self, request, pk, comment_id):
        try:
            video = Video.objects.filter(pk=pk).first()
            comment = Comment.objects.filter(pk=comment_id).first()
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            # comment = Comment.objects.filter(articles=article)
            serializer = CommentChildSerializer(comment)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = CommentCreateSerializers(data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save(owner=request.user, parent=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        
