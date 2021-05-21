from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .viewsets import ArticleViewSets

router = DefaultRouter()
router.register(r'articles', ArticleViewSets, basename='articles')

# routerS = routers.SimpleRouter()
# routerS.register(r'mix-data', ArticleViewSets, basename='mix-data')



