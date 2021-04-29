from django import http
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action, api_view, permission_classes

from ..models import Articles
from .serializers import ArticleSerializers, ArticleCreateSerializers
from comments.models import Comment
from comments.api.serializers import *


class ArticleViewSets(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset

    def create(self, request):
        
        serializer = ArticleCreateSerializers(data=request, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save(owner=request.user)
        return Response(serializer.data)


    @action(detail=False, methods=['POST','GET'])
    def comments(self, request, pk):
        article = Articles.objects.filter(pk=pk).first()
        self.serializer_class = CommentSerializers
        queryset = Comment.objects.filter(articles=article)
        if article:
            if request.method == 'GET':
                if queryset:
                    serializer = CommentSerializers(queryset, many=True, context={'request':request})
                    return Response(serializer.data)
                return Response({'message': 'comment not founded'})
            else:
                print(request.data, 'neser')
                serializer = CommentCreateSerializers(data=request.data, context={'request':request})
                serializer.is_valid(raise_exception=True)
                serializer.save(owner=request.user, articles=article)
                return Response(serializer.data)
        return Response({'message': 'article not founded'}, status=404)

    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment_id):
        comment = Comment.objects.filter(pk=comment_id)
        if comment:
            if comment.delete():
                return Response({'message':'Comment deleted'}, status=204)
            else:
                return Response({'message':'unable to delete comment'}, status=400)
        return Response({'message': 'comment not founded'}, status=404)

    @action(detail=False, methods=['GET', 'POST'])
    def reply_comment(self, request, pk, comment_id):
        try:
            article = Articles.objects.filter(pk=pk).first()
            comment = Comment.objects.filter(pk=comment_id).first()
        except Articles.DoesNotExist:
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
