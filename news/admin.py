from django.contrib import admin
from .models import News
# Register your models here.


# class Inline(admin.TabularInline):
#     '''Tabular Inline View for '''

#     model = 
#     min_num = 3
#     max_num = 20
#     extra = 1
#     raw_id_fields = (,)

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
