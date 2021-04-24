from rest_framework import serializers
from ..models import Articles

from account.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

from main.api.serializers import TagSerializer
from main.models import Tag

User = get_user_model()


class ArticleSerializers(serializers.ModelSerializer):
    # owner = UserSerializer()
    owner = serializers.StringRelatedField()
    tag = serializers.SerializerMethodField()
    
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

    def get_tag(self, obj):
        tags = obj.tag
        return TagSerializer(tags, many=True).data

class ArticleCreateSerializers(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    print(owner, 'malas')
    
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
        