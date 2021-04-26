from django.urls import path
from django.conf.urls import url
from .routers import router
from .viewsets import ArticleViewSets



urlpatterns = [
    # path('articles/(?P<pk>)/comments/', view=ArticleViewSets.as_view({'get':'comments', 'post':'comments'})),
    # path('articles/(?P<pk>)/comments/(?P<comment>\d+)/', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    url(r'articles/(?P<pk>\d+)/comments/$', view=ArticleViewSets.as_view({'get':'comments', 'post':'comments'})),
    url(r'articles/(?P<pk>\d+)/comments/(?P<comment>\d+)/$', view=ArticleViewSets.as_view({'delete':'remove_comment'}))
]

urlpatterns += router.urls
