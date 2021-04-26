from rest_framework import serializers
from ..models import Comment
from account.api.serializers import *


class CommentSerializers(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    news = serializers.StringRelatedField()
    videos = serializers.StringRelatedField()

    
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'content', 'news', 'videos', 'articles']

class CommentCreateSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = Comment
        fields = ['id', 'content', 'news', 'videos', 'articles']