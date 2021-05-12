from rest_framework import serializers
from ..models import Comment
from account.api.serializers import *
from articles.models import Articles


class CommentChildSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    replies = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'parent',
            'content',
            'reply_count',
            'replies',
            'created_at',
        ]

    def get_owner(self, obj):
        return obj.owner.username


    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_replies(self, obj):
        if obj.children():
            return CommentChildSerializer(obj.children(), many=True).data
        return []

class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # news = serializers.StringRelatedField()
    # videos = serializers.StringRelatedField()
    # articles = serializers.PrimaryKeyRelatedField(queryset= Articles.objects.all() if Articles.objects.all() else {}, required=False)
    reply_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    
    class Meta:
        model = Comment
        fields = ['id', 'category', 'owner', 'content', 'reply_count', 'replies']

    def get_reply_count(self, obj):
        if obj.children():
            return obj.children().count()
        return 0

    def get_category(self, obj):
        return obj.get_category()
    
    def get_owner(self, obj):
        return obj.owner.username

    def get_replies(self, obj):
        if obj.children():
            return CommentChildSerializer(obj.children(), many=True).data
        return []
        # if obj.is_parent:
        #     return CommentChildSerializer(obj.children(), many=True)
        # return None

class CommentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'news', 'videos', 'articles']


