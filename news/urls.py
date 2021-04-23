from django.urls import path, include


app_name = 'news'

urlpatterns = [
    path('api/v1.0/', include('news.api.urls'))
]