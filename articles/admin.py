from django.contrib import admin
from .models import Articles
# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'is_published', )
    list_display_links = ("title",)
    list_filter = ("title", "category")
    search_fields = ('title',)

    readonly_fields = (
        'created_at',
    )
    fieldsets = (
        ('Informations', {
            'fields': ("id", "owner", "title", "short_desc", "content",  "views", 'category', "is_published", )
        }),
    )
