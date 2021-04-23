from django.urls import path, include


app_name = 'articles'

urlpatterns = [
    path('', include('articles.api.urls'))
]