from django.contrib import admin
from .models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'owner', )
    list_display_links = ("title",)
    list_filter = ("title", "tag")
    search_fields = ('title',)

    readonly_fields = (
        'created_at',
    )
    fieldsets = (
        ('Informations', {
            'fields': ("owner", "title", "short_desc", "content", "image", "cover_image", "video_link", "views", 'tag', "is_published", )
        }),
    )
