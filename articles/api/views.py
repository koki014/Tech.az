from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import *
from news.models import *
from videos.models import *
from articles.api.serializers  import *
from news.api.serializers import *
from videos.api.serializers  import *
import json
import pprint

class AllData(APIView):

    def get(self, request, **kwargs):

        news = News.objects.all()
        articles = Articles.objects.all()
        video = Video.objects.all()
        news_list = NewsSerializers(news, many=True)
        articles_list = ArticleSerializers(articles, many=True)
        video_list = VideoSerializers(video, many=True)
        news_list = json.loads(json.dumps(news_list.data))
        print(type(news_list[0]))
        print(*news_list)
     
        
        

        # print(json.loads(news_data), 'sasasasa')
        return Response({})
        # return Response({
        #     'data':{
        #         *news_dict,
        #         #**articles_list.data,
        #         #**video_list.data
        # }
        # })
    