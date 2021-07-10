from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    # from articles.api.serializers import ArticleSerializers
    token = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()
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
            'birthday',
            'token',
            'articles'
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'username': {'required': True},
        }
    
    def get_token(self, user):
        request = self.context.get('request')
        if request and hasattr(request, 'META') and request.META.get('HTTP_AUTHORIZATION'):
            header_token = request.META.get('HTTP_AUTHORIZATION')
            return header_token.split()[1]
        token, created = Token.objects.get_or_create(user=user)
        return token.key

    def get_articles(self, obj):
        from articles.api.serializers import ArticleSerializers
        articles_list = obj.articles.all()
        return ArticleSerializers(articles_list, many=True).data

class UserSerializerCreate(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, label='Confirm password'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'education', 'position', 'birthday',
                'image', 'created_at', 'updated_at',]
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'username': {'required': True}
        }

    def create(self, validated_data):
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        position = validated_data.get('position', '')
        education = validated_data.get('education', '')
        birthday = validated_data.get('birthday', '')
        image = validated_data.get('image', '')
        username = validated_data.get('username', '')
        email = validated_data.get('email', '')
        password = validated_data.get('password', '')
        password2 = validated_data.get('password2', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Bu email artiq movcuddur.'}
            )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': 'Bu username artiq movcuddur.'}
            )
        
        if password != password2:
            raise serializers.ValidationError({'password': 'The two passwords differ.'})
        user = User(username=username, email=email, first_name=first_name, last_name=last_name,
                    position=position, image=image, education=education, birthday=birthday)
        user.set_password(password)
        user.save()
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):

    def validate_email(self, value):
        request = self.context.get('request')
        user = request.user
        if value != user.email:
            raise serializers.ValidationError(_("You can not change your email"))
        return value

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'education', 'position', 'image','birthday',]
