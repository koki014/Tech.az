# from sys import path
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from articles.models import *
# from news.models import *
# from videos.models import *
# from articles.api.serializers  import *
# from news.api.serializers import *
# from videos.api.serializers  import *
# import json


# class AllData(APIView):

#     def get(self, request, **kwargs):

#         news = News.objects.all()
#         articles = Articles.objects.all()
#         video = Video.objects.all()
#         news_list = NewsSerializers(news, many=True)
#         articles_list = ArticleSerializers(articles, many=True)
#         video_list = VideoSerializers(video, many=True)
#         news_list = json.loads(json.dumps(news_list.data))
#         articles_list = json.loads(json.dumps(articles_list.data))
#         video_list = json.loads(json.dumps(video_list.data))
        

#         newlist = sorted(news_list, key=lambda k: k['created_at'], reverse=True)
#         # articleslist = sorted(articles_list, key=lambda k : k['created_at'], reverse=True)
#         # videolist = sorted(video_list, key=lambda k : k['created_at'], reverse=True)
#         print(articles_list)
#         datas = []
#         datas.extend(newlist)
#         # datas.extend(articleslist)
#         # datas.extend(videolist)
#         print(datas)

#         print(newlist)
     
        
        

#         # print(json.loads(news_data), 'sasasasa')

#         return Response({})
#         # return Response({
#         #     'data':{
#         #         **news_list,
#         #         #**articles_list.data,
#         #         #**video_list.data
#         # }
#         # })
    