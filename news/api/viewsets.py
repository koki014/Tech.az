from rest_framework import permissions
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from ..models import News
from .paginations import LimitPagination

from comments.models import Comment
from comments.api.serializers import *

class NewsViewSets(ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny,]
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsSerializers
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }
    pagination_class = LimitPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset
    

    def retrieve(self, request, slug=None):
        news = get_object_or_404(News,slug=slug)
        news.add_view_count()
        serializer = NewsSerializers(news)
        return Response(serializer.data)


    # def create(self, request):
    #     serializer = NewsCreateSerializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=False)
    #     if request.user:
    #         serializer.save(owner=request.user)
    #     # serializer.save()
    #     return Response(serializer.data)

    
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
                return Response({'message': 'comment not founded'}, status=404)
            else:
                print(request.data, 'lalar')
                if request.data:
                    serializer = CommentCreateSerializers(data=request.data, context={'request': request})
                    serializer.is_valid(raise_exception=False)
                    serializer.save(owner=request.user, news=news)
                    return Response(serializer.data, status=201)
                return Response({'content': 'this field required'})
        return Response({'message': 'news not founded'}, status=404)

    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment_id):
        comment = Comment.objects.filter(pk=comment_id)
        if comment:
            if comment.delete():
                return Response({'message':'Comment deleted'}, status=204)
            else:
                return Response({'message': 'unable to delete comment'}, status=204)
        return Response({'message': 'comment not founded'}, status=404)
    
    @action(detail=False, methods=['GET', 'POST'])
    def reply_comment(self, request, pk, comment_id):
        try:
            new = News.objects.filter(pk=pk).first()
            comment = Comment.objects.filter(pk=comment_id).first()
        except News.DoesNotExist:
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

