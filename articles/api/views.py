
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import *
from news.models import *
from videos.models import *
from articles.api.serializers  import *
from news.api.serializers import *
from videos.api.serializers  import *
import json
from itertools import chain
from drf_multiple_model.views import ObjectMultipleModelAPIView


# class MixData(APIView):

#     def get(self, request, **kwargs):

#         news = News.objects.all()
#         articles = Articles.objects.all()
#         video = Video.objects.all()
#         news_list = NewsSerializers(news, many=True)
#         articles_list = ArticleSerializers(articles, many=True)
#         # video_list = VideoSerializers(video, many=True)
#         # news_list = json.dumps(news_list)
#         # articles_list = json.dumps(articles_list)

#         orders = list(
#                     sorted(
#                         chain(news, articles),
#                         key=lambda objects: objects.created_at
#                     ))
#         # paginator = Paginator(orders, 5)
                
#         return Response({
#             'data': orders
#         })
    

class MixData(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': News.objects.all().order_by('-created_at'), 'serializer_class': NewsSerializers},
        {'queryset': Articles.objects.all().order_by('-created_at'), 'serializer_class': ArticleSerializers},
    ]
    