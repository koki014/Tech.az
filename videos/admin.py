from django.contrib import admin
from .models import Video, VideosImage
# Register your models here.

@admin.register(VideosImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", 'is_published')

class ImageInline(admin.TabularInline):
    model = VideosImage


@admin.register(Video)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'owner', )
    list_display_links = ("title",)
    list_filter = ("title", "tag")
    search_fields = ('title',)
    inlines = (ImageInline,)

    readonly_fields = (
        'created_at',
    )
    fieldsets = (
        ('Informations', {
            'fields': ("owner", "title", "short_desc", "content","cover_image", "video_link", "views", 'tag', "is_published", )
        }),
    )
