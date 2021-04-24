from rest_framework import serializers
from ..models import Articles

from account.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

from main.api.serializers import TagSerializer

User = get_user_model()


class ArticleSerializers(serializers.ModelSerializer):
    tag = TagSerializer()
    owner = UserSerializer()
    
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

class ArticleCreateSerializers(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    tag = TagSerializer(read_only=True, many=True)
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

    def validate(self, data):
        request = self.context.get('request')
        data['owner'] = request.user
        return super().validate(data)