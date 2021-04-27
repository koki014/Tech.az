from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes

from ..models import Articles
from .serializers import ArticleSerializers, ArticleCreateSerializers
from comments.models import Comment
from comments.api.serializers import *


class ArticleViewSets(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # serializers = {
    #     'list': ArticleSerializers,
    #     'retrieve': ArticleSerializers,
    #     'default': ArticleCreateSerializers
    # }

    # def get_serializer_class(self):
    #     return self.serializers.get(self.action, self.serializers.get('default'))

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.GET.get('owner_id')
        if owner:
            queryset = queryset.filter(owner=owner)
        return queryset

    def create(self, request):
        serializer = ArticleCreateSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save(owner=request.user)
        return Response(serializer.data)


    @action(detail=False, methods=['POST','GET'])
    def comments(self, request, pk):
        article = Articles.objects.filter(pk=pk).first()
        self.serializer_class = CommentSerializers
        queryset = Comment.objects.filter(articles=article).first();
        if article:
            if request.method == 'GET':
                if queryset:
                    serializer = CommentSerializers(queryset, many=True, context={'request':request})
                    return Response(serializer.data)
                return Response({'message': 'comment not founded'})
            else:
                serializer = CommentCreateSerializers(data=request.data, context={'request':request})
                serializer.is_valid(raise_exception=True)
                serializer.save(owner=request.user, articles=article)
                return Response(serializer.data)
        return Response({'message': 'article not founded'})

    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment):
        comment = Comment.objects.filter(pk=comment)
        if comment:
            if comment.delete():
                return Response({'message':'Comment deleted'})
            else:
                return Response({'message':'unable to delete comment'})
        return Response({'message': 'comment not founded'})

    # @action(detail=False, method=['GET', "POST"])
    # def reply_comment(self, request, pk, comment):
    #     comment = Comment.objects.get(pk=comment)
    #     if request.method == 'GET':
    #         self.serializer_class = C