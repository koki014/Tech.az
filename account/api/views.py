from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserSerializerCreate, ProfileUpdateSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from articles.api.serializers import ArticleSerializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from account.utils import CustomSwaggerAutoSchema


User = get_user_model()


class LoginAPI(ObtainAuthToken):
    custom_serializer_class = UserSerializer

    @swagger_auto_schema(auto_schema=CustomSwaggerAutoSchema, request_body=AuthTokenSerializer, responses={200: custom_serializer_class})
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = self.custom_serializer_class(user, context={'request': request})
        return Response(user_serializer.data)

class ProfileAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    update_serializer_class = ProfileUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(data=self.serializer_class(request.user, context={'request': request}).data)

    
    @swagger_auto_schema(request_body=update_serializer_class, responses={200: UserSerializer})
    def put(self, request):
        data = request.data
        serializer = self.update_serializer_class(request.user, data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        updated_user = serializer.save()
        return Response(data=self.serializer_class(updated_user, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=update_serializer_class, responses={200: UserSerializer})
    def patch(self, request):
        data = request.data
        serializer = self.update_serializer_class(request.user, data=data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        updated_user = serializer.save()
        return Response(data=self.serializer_class(updated_user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class RegisterAPIView(CreateAPIView):
    model = User
    serializer_class = UserSerializerCreate

    @swagger_auto_schema(request_body=UserSerializerCreate)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    queryset = User.objects.filter(status=True)
    # permission_classes = (permissions.IsAuthenticated,)

    def get_users_news(self, request, user_id=None, *args, **kwargs):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=user_id)
        articles = user.articles.all()
        serializer =  ArticleSerializers(articles, many=True, context={'request': request})
        if articles:
            return Response(serializer.data)
        return Response({'message': 'Not founded'})