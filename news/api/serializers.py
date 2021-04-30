from rest_framework import serializers
from ..models import News
from account.api.serializers import UserSerializer
from main.api.serializers import TagSerializer
from django.contrib.auth import get_user_model
from .serializers import *
from comments.api.serializers import *
User = get_user_model()


class NewsSerializers(serializers.ModelSerializer):
    # tag = TagSerializer(many=True)
    tag = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    # owner = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = [
            'id',
            'owner',
            'tag',
            'title',
            'short_desc',
            'content',
            'image',
            'cover_image',
            'video_link',
            'comments',
            'views',
            'created_at'
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
    
    def get_owner(self, obj):
        return obj.owner.username

    def get_comments(self, obj):
        news_comments = obj.news_comments
        return CommentSerializers(news_comments, many=True).data

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data


class NewsCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = News
        extra_kwargs = {'tag': {'required': False}}

        fields = [
            'id',
            'owner',
            'tag',
            'title',
            'short_desc',
            'content',
            'image',
            'cover_image',
            'video_link',
            # 'comments',
            'views',
            'created_at'
        ]

    

    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        return super().validate(data)
