from rest_framework import serializers
from ..models import Articles

from account.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

from main.api.serializers import TagSerializer
from main.models import Tag
from comments.api.serializers import CommentSerializers

User = get_user_model()


class ArticleSerializers(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    # owner = serializers.StringRelatedField()
    tag = serializers.SerializerMethodField()
    articles_comments = serializers.SerializerMethodField()
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
            'articles_comments'
        ]
        extra_kwargs = {'tag': {'required': False}}

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data

    def get_articles_comments(self, obj):
        tags = obj.articles_comments
        return CommentSerializers(tags, many=True).data

class ArticleCreateSerializers(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

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
        ]
        extra_kwargs = {'tag': {'required': False}}

    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        return super().validate(data)
        