from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import News, NewsImage
from account.api.serializers import UserSerializer
from main.api.serializers import TagSerializer
from django.contrib.auth import get_user_model
from django.conf import settings

from .serializers import *
from comments.api.serializers import *
User = get_user_model()



class NewImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = (
            'image',
            )


class NewsSerializers(serializers.ModelSerializer):
    # file_abs_url = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    news_images = NewImageSerializers(many=True)
    # owner = UserSerializer(read_only=True)
    owner = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()
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
            'news_images',
            'cover_image',
            'video_link',
            'comments',
            'views',
            'slug',
            'file_abs_url',
            'created_at',
        ]



    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
    
    # def get_owner(self, obj):
    #     return obj.owner.username

    def get_comments(self, obj):
        news_comments = obj.news_comments
        return CommentSerializers(news_comments, many=True).data

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data
    
    # def get_file_abs_url(self, obj):
    #     request = self.context.get('request')
    #     if request:
    #         return request.build_absolute_uri(obj.slug)
    #     return settings.SITE_ADDRESS + '/api/news/' + obj.slug +'/'

# class NewsCreateSerializer(serializers.ModelSerializer):
#     # owner = serializers.PrimaryKeyRelatedField(queryset= User.objects.all() if User.objects.all() else {}, required=False)
    
#     owner = UserSerializer(read_only=True)
#     class Meta:
#         model = News
#         extra_kwargs = {'tag': {'required': False}}

#         fields = [
#             'id',
#             'owner',
#             'tag',
#             'title',
#             'short_desc',
#             'content',
#             'image',
#             'cover_image',
#             'video_link',
#             'views',
#             'created_at'
#         ]

    

#     def validate(self, data):
#         request = self.context.get('request')
#         data['owner'] = request.user
#         return super().validate(data)


