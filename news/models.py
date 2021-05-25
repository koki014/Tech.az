from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from main.models import Tag

from tech.commons import slugify

User = get_user_model()


class News(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='news')

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Qısa Məzmun", max_length=256)
    content = models.TextField('Məzmun')
    cover_image = models.ImageField("Qapak örtüyü", upload_to='cover_images', null=True, blank=True)
    video_link = models.URLField(max_length=300, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)
    file_abs_url = models.URLField(_("abs url"), default='', max_length=200)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Xəbər'
        verbose_name_plural = 'Xeberler'
        ordering = ('-created_at',)

    def add_view_count(self):
        self.views +=4
        self.save()
        return True

    # def save(self, *args, **kwargs):
        
    #     news = News.objects.filter(title=self.title).first()
    #     if not news: 
    #         self.slug = slugify(f'{self.title}')
    #     else:
    #         super(News, self).save(*args, **kwargs)
    #         self.slug = f'{slugify(self.title)}-{self.id}'
    #     self.file_abs_url = f'{settings.SITE_ADDRESS}/api/news/{self.slug}/'
    #     super(News, self).save(*args, **kwargs)


class NewsImage(models.Model):

    # relation's
    news = models.ForeignKey("news.News", related_name='news_images', on_delete=models.CASCADE, blank=True, null=True)

    # informations
    image = models.ImageField(_("Image"), upload_to='news_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Xəbər Şəkili'
        verbose_name_plural = 'Xəbərlərin Şəkilləri'
        ordering = ('-created_at',)
