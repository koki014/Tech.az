from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import *
from ..models import News
from comments.models import Comment
from comments.api.serializers import *

class NewsViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset

    def create(self, request):
        serializer = NewsCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=False)
        if request.user:
            serializer.save(owner=request.user)
        serializer.save()
        return Response(serializer.data)

    
    @action(detail=False, methods=['GET', 'POST'])
    def comments(self, request, pk):
        print(pk, 'idler')
        news = News.objects.filter(pk=pk).first()
        self.serializer_class = CommentSerializers
        queryset = Comment.objects.filter(news=news).first()
        if news:
            if request.method == 'GET':
                if queryset:
                    serializer = CommentSerializers(queryset, context={'request': request})
                    return Response(serializer.data)
                return Response({'message': 'comment not founded'})
            else:
                print(request.data, 'lalar')
                if request.data:
                    serializer = CommentCreateSerializers(data=request.data, context={'request': request})
                    serializer.is_valid(raise_exception=False)
                    serializer.save(owner=request.user, news=news)
                    return Response(serializer.data)
                return Response({'content': 'this field required'})
        return Response({'message': 'news not founded'})

    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment_id):
        comment = Comment.objects.filter(pk=comment_id)
        if comment:
            if comment.delete():
                return Response({'message':'Comment deleted'})
            else:
                return Response({'message': 'unable to delete comment'})
        return Response({'message': 'comment not founded'})

