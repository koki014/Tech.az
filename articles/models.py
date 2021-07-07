from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from main.models import Tag

from tech.commons import slugify

User = get_user_model()

# Create your models here.

class Articles(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    tag = models.ManyToManyField(Tag, related_name='articles')

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Qisa mezmun", max_length=256)
    content = models.TextField('Mezmun')
    image = models.ImageField("Şəkil", upload_to='article_images', null=True, blank=True)
    cover_image = models.ImageField("Qapak örtüyü", upload_to='aritcle_cover_images', null=True, blank=True)
    views = models.PositiveIntegerField(default=3, blank=True, null=True)
    slug = models.SlugField('Slug', max_length=110, unique=True)
    file_abs_url = models.URLField(_("abs url"), default='', max_length=200)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Megale'
        verbose_name_plural = 'Megaleler'
        ordering = ('-created_at',)

    def add_view_count(self):
        self.views +=4
        self.save()
        return True

    # def save(self, *args, **kwargs):
    #     super(Articles, self).save(*args, **kwargs)    
    #     self.slug = f'{slugify(self.title)}-{self.id}'
    #     super(Articles, self).save(*args, **kwargs)
    


# class ArticleImage(models.Model):

#     # relation's
#     articles = models.ForeignKey(Articles, related_name='articles_images', on_delete=models.CASCADE, blank=True, null=True)

#     # informations
#     image = models.ImageField(_("Image"), upload_to='articles_images')

#     # moderations
#     is_published = models.BooleanField('is published', default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'Məqalə Şəkili'
#         verbose_name_plural = 'Məqalələrin Şəkilləri'
#         ordering = ('-created_at',)
