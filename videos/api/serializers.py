from rest_framework import serializers
from account.api.serializers import UserSerializer
from main.api.serializers import TagSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

from ..models import Video

class VideoSerializers(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    tag = serializers.SerializerMethodField()

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

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data
    

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