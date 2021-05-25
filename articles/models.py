from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from main.models import Tag

from tech.commons import slugify

User = get_user_model()

# Create your models here.



class Articles(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='articles')

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Qisa mezmun", max_length=256)
    content = models.TextField('Mezmun')
    cover_image = models.ImageField("Qapak örtüyü", upload_to='cover_images', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField('Slug', max_length=110, unique = True)

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

    def save(self, *args, **kwargs):
        # super(Articles, self).save(*args, **kwargs)
        articles = Articles.objects.filter(title=self.title).first()
        print(len(self.slug), 'salamnn')
        if not articles: 
            self.slug = slugify(f'{self.title}')
        else:
            print('girmedi')
            self.slug = f'{slugify(self.title)}-{self.id}'
        super(Articles, self).save(*args, **kwargs)


class ArticleImage(models.Model):

    # relation's
    articles = models.ForeignKey(Articles, related_name='articles_images', on_delete=models.CASCADE, blank=True, null=True)

    # informations
    image = models.ImageField(_("Image"), upload_to='news_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Məqalə Şəkili'
        verbose_name_plural = 'Məqalələrin Şəkilləri'
        ordering = ('-created_at',)
