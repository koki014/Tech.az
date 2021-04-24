from django.db import models
from django.contrib.auth import get_user_model
from main.models import Tag

from tech.commons import slugify

User = get_user_model()


class News(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Qısa Məzmun", max_length=256)
    content = models.TextField('Məzmun')
    image = models.ImageField("Şəkil", upload_to='news_images', null=True, blank=True)
    cover_image = models.ImageField("Qapak örtüyü", upload_to='cover_images', null=True, blank=True)
    video_link = models.URLField(max_length=300, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Xeber'
        verbose_name_plural = 'Xeberler'
        ordering = ('-created_at',)

    def add_view_count(self):
        self.views +=4
        self.save()
        return True

    def save(self, *args, **kwargs):
        news = News.objects.filter(title=self.title).first()

        if not news: 
            self.slug = slugify(f'{self.title}')
        else:
            print('girmedi')
            self.slug = f'{slugify(self.title)}-{news.created_at.timestamp()}'
        super(News, self).save(*args, **kwargs)
