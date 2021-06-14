"""tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Tech.az"
admin.site.site_title = "Tech.az"
admin.site.index_title = "Tech.az"

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi





schema_view = get_schema_view(
    openapi.Info(
        title="Tech Az API",
        default_version='version 1',
        description="All API enpoints",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="techaz.@gmail.com"),
        license=openapi.License(name="No License Yet"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # re_path(r'^swa$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', admin.site.urls),
    path('api-doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('account.urls', namespace='account')),
    path('api/', include('articles.urls', namespace='articles')),
    path('api/', include('news.urls', namespace='news')),
    path('api/', include('comments.urls', namespace='comments')),
    path('api/', include('videos.urls', namespace='video')),
    path('api/', include('main.urls'))



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



