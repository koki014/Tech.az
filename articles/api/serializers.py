from rest_framework import serializers
from ..models import *

from account.api.serializers import UserSerializer
from django.contrib.auth import get_user_model


from main.api.serializers import TagSerializer
from main.models import Tag
from comments.api.serializers import CommentSerializers
from news.api.serializers import *
from videos.api.serializers import *

User = get_user_model()





# class ArticleImageSerializer(serializers.ModelSerializer):
#     model = ArticleImage
#     image = Base64ImageField()
#     fields = [
#         'id',
#         'image',
#         'created_at',
#     ]


class ArticleSerializers(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)
    owner = serializers.StringRelatedField()
    tag = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    # images = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields  = [
            'id',
            'owner',
            'tag',
            'title',
            'short_desc',
            'content',
            'image',
            'cover_image',
            'views',
            'file_abs_url',
            'created_at',
            'slug',
            'comments',
        ]
        extra_kwargs = {'tag': {'required': False}}

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data

    # def get_images(self, obj):
    #     data = obj.articles_images
    #     return ArticleImageSerializer(data, many=True).data

    def get_owner(self, obj):
        return obj.owner.username


    def get_comments(self, obj):
        comment = obj.articles_comments
        return CommentSerializers(comment, many=True).data

class ArticleCreateSerializers(serializers.ModelSerializer):
    owner=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

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
        print('herer')
        data['owner'] = request.user
        print(request.user)
        return super().validate(data)
    

    # def create(self, validated_data):
    #     print(validated_data)
    #     images = validated_data.pop('articles_images')
    #     print(images, 'sekil')
    #     print(validated_data)
    #     instance = super().create(validated_data)
        
    #     for image in images:
    #         print(image, 'imagess')
    #         image_serializer = ArticleImageSerializer(**image)
    #         image_serializer.is_valid(raise_exception=True)
    #         image_serializer.save(articles=instance)
    #     return instance
    




