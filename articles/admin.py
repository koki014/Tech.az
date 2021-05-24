from django.contrib import admin
from .models import Articles, ArticleImage
# Register your models here.

admin.site.register(ArticleImage)
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'is_published', 'slug',)
    list_display_links = ("title",)
    list_filter = ("title", "tag")
    search_fields = ('title',)
    # readonly_fields = ('slug',)

    readonly_fields = (
        'created_at',
    )
    fieldsets = (
        ('Informations', {
            'fields': ("owner", "title", "short_desc", "content",  "views", 'tag','slug', "is_published", )
        }),
    )
