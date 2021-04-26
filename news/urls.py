from django.urls import path, include


app_name = 'news'

urlpatterns = [
    path('', include('news.api.urls'))
]