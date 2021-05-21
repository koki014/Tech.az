
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import *
from news.models import *
from videos.models import *
from articles.api.serializers  import *
from news.api.serializers import *
from videos.api.serializers  import *

from drf_multiple_model.views import FlatMultipleModelAPIView





class MixData(FlatMultipleModelAPIView):
    sorting_fields = ['-created_at']
    querylist = [
        {'queryset': News.objects.all(), 'serializer_class': NewsSerializers, 'label': 'News'},
        {'queryset': Articles.objects.all(), 'serializer_class': ArticleSerializers, 'label': 'Articles'},
    ]
    