from rest_framework import serializers
from account.api.serializers import UserSerializer
from main.api.serializers import TagSerializer
from comments.api.serializers import CommentSerializers
from django.contrib.auth import get_user_model
User = get_user_model()

from ..models import Video

class VideoSerializers(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner = serializers.StringRelatedField()
    tag = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    

    class Meta:
        model = Video
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
            'comments',
            'created_at'
            ]

        extra_kwargs = {
            'tag': {'required': False},
            }

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data
    
    def get_owner(self, obj):
        return obj.owner.username
    
    def get_comments(self, obj):
        comment = obj.videos_comments
        return CommentSerializers(comment, many=True).data
    

class VideoCreateSerializers(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Video
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

        extra_kwargs = {'tag': {'required': False}}

    
    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        return super().validate(data)