from django.conf import settings
from rest_framework import serializers
from ..models import News, NewsImage
from account.api.serializers import UserSerializer
from main.api.serializers import TagSerializer
from django.contrib.auth import get_user_model
from .serializers import *
from comments.api.serializers import *


User = get_user_model()



class NewsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = [
            'id',
            'title',
            'image_url',
            'is_published',
            'created_at',
        ]


class NewsSerializers(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    comments = serializers.SerializerMethodField()
    news_image = serializers.SerializerMethodField(read_only=True, required=False)
    # absolute_url = serializers.SerializerMethodField()

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
            'news_image',
            'video_link',
            'comments',
            'views',
            'slug',
            'created_at',
        ]

    def get_news_image(self, obj):
        data = obj.news_images.all()
        return NewsImageSerializers(data, many=True).data


    def get_image(self, obj):
        try:
            image = "{0}{1}".format(settings.SITE_ADDRESS, obj.image.url)
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
    # owner = serializers.PrimaryKeyRelatedField(queryset= User.objects.all() if User.objects.all() else {}, required=False)
    
    owner = UserSerializer(read_only=True)
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
            'views',
            'created_at'
        ]

    

    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        return super().validate(data)
