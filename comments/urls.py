from django.urls import path, include


app_name = 'comments'

urlpatterns = [
    path("", include('comments.api.urls'))
]
