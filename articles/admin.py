from django.contrib import admin
from .models import Articles
# Register your models here.


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'is_published', 'slug',)
    list_display_links = ("title",)
    list_filter = ("title", "tag")
    search_fields = ('title',)
    readonly_fields = ('slug',)
    save_on_top = True
    readonly_fields = (
        'created_at',
    )
    fieldsets = (
        ('Informations', {
            'fields': ("owner", "title", "short_desc", "content",  "views", 'tag', "is_published", "cover_image", )
        }),
    )
