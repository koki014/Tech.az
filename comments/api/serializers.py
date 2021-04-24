from rest_framework import serializers

from ..models import Comment


class CommentSerializers(serializers.ModelSerializer):
    news = serializers.StringRelatedField()
    videos = serializers.StringRelatedField()
    articles = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'news', 'videos', 'articles']


class CommentCreateSerializers(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'content', 'news', 'videos', 'articles']