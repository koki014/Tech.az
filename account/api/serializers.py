from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'education',
            'position',
            'image',
            'cover_image',
            'birthday'
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'username': {'required': True},
        }


class UserSerializerCreate(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, label='Confirm password'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'education', 'position',
                'image', 'cover_image', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}