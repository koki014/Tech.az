from django.urls import path, include

app_name = 'videos'

urlpatterns = [
    path('', include('videos.api.urls'))
]
