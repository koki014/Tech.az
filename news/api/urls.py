
from django.urls import path
from django.conf.urls import url
from .routers import router
from .viewsets import NewsViewSet





urlpatterns = [
    url(r'news/(?P<pk>\d+)/comments/$', view=NewsViewSet.as_view({'get':'comments', 'post':'comments'})),
    url(r'news/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=NewsViewSet.as_view({'delete':'remove_comment'})),
]
urlpatterns += router.urlsz