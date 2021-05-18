from rest_framework import serializers
from ..models import Articles

from account.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

from main.api.serializers import TagSerializer
from main.models import Tag
from comments.api.serializers import CommentSerializers
from news.api.serializers import *
from videos.api.serializers import *

User = get_user_model()


# articles_detail_url = serializers.HyperlinkedIdentityField(
#     view_name='app_name:view_name',
#     lookup_field='slug'
# )

class ArticleSerializers(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner = serializers.StringRelatedField()
    tag = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields  = [
            'id',
            'title',
            'short_desc',
            'content',
            'views',
            'owner',
            'tag',
            
            'comments'
        ]
        extra_kwargs = {'tag': {'required': False}}

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data

    def get_owner(self, obj):
        return obj.owner.username


    def get_comments(self, obj):
        comment = obj.articles_comments
        return CommentSerializers(comment, many=True).data

class ArticleCreateSerializers(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Articles
        extra_kwargs = { 'tag': {'required': False} } 
        fields  = [
            'id',
            'title',
            'short_desc',
            'content',
            'views',
            'owner',
            'tag',
        ]

    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        return super().validate(data)
    


# class AllDataSerializers(serializers.ModelSerializer):
#     articles = ArticleSerializers(read_only=True)
