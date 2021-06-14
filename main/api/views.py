
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from main.api.serializers import *
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .serializers import JoinSerializer, TagSerializer



class JoinAPIView(APIView):
    queryset = Join.objects.all()
    
    def get(self, request, *args, **kwargs):
        joins = Join.objects.all()
        serilizer = JoinSerializer(joins, many=True, context = {'request' : request})
        return Response(data=serilizer.data, status=HTTP_200_OK)


    def post(self, request, *args, **kwargs):
            recipe_data = request.data
            serializer = JoinCreateSerializer(data=recipe_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)


class TagViewsSet(ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(is_published=True)