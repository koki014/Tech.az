from rest_framework.routers import DefaultRouter

from .viewsets import ArticleViewSets

router = DefaultRouter()
router.register(r'articles', ArticleViewSets, basename='articles')



