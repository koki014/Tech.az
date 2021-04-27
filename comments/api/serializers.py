from rest_framework import serializers
from ..models import Comment
from account.api.serializers import *
from articles.models import Articles


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    news = serializers.StringRelatedField()
    videos = serializers.StringRelatedField()
    articles = serializers.PrimaryKeyRelatedField(queryset= Articles.objects.all() if Articles.objects.all() else {}, required=False)
    reply_count = serializers.SerializerMethodField()

    
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'content', 'reply_count', 'news', 'videos', 'articles']

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
    
    def get_owner(self, obj):
        return obj.owner.username

class CommentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'news', 'videos', 'articles']
