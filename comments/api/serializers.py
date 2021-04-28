from rest_framework import serializers
from ..models import Comment
from account.api.serializers import *
from articles.models import Articles


class CommentChildSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'parent',
            'content',
            'reply_count',
            'replies',
            'created_at'
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            print(obj.children(), 'balalar')
            return obj.children().count()
        return 0

    def get_replies(self, obj):
        return CommentChildSerializer(obj.children(), many=True).data


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    news = serializers.StringRelatedField()
    videos = serializers.StringRelatedField()
    articles = serializers.PrimaryKeyRelatedField(queryset= Articles.objects.all() if Articles.objects.all() else {}, required=False)
    reply_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'content', 'reply_count', 'replies', 'news', 'videos', 'articles']

    def get_reply_count(self, obj):
        if obj.children():
            return obj.children().count()
        return 0
    
    def get_owner(self, obj):
        return obj.owner.username

    def get_replies(self, obj):
        if obj.children():
            return CommentChildSerializer(obj.children(), many=True).data
        # if obj.is_parent:
        #     return CommentChildSerializer(obj.children(), many=True)
        # return None

class CommentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'news', 'videos', 'articles']


