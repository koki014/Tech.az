from django.db import models
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
    short_desc = models.CharField("Basliq", max_length=256)
    content = models.TextField('Mezmun')
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)

    # moderations
    is_published = models.BooleanField('is published', default=False)
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
        news = Articles.objects.filter(title=self.title).first()
        # print(len(self.slug), 'salamnn')

        if not news: 
            print('girdi')
            self.slug = slugify(f'{self.title}')
        else:
            print('girmedi')
            self.slug = f'{slugify(self.title)}-{news.created_at.strftime("%s")}'
        super(Articles, self).save(*args, **kwargs)

