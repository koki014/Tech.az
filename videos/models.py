from django.db import models
from django.contrib.auth import get_user_model
from main.models import Tag

from tech.commons import slugify

User = get_user_model()


class Video(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Basliq", max_length=256)
    content = models.TextField('Mezmun')
    image = models.ImageField("Image", upload_to='video_images')
    cover_image = models.ImageField("Image", upload_to='cover_images')
    video_link = models.URLField(max_length=300, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'
        ordering = ('-created_at',)

    def add_view_count(self):
        self.views +=4
        self.save()
        return True

    def save(self):
        news = Video.objects.filter(title=self.title).first()
        super(self).save(*args, **kwargs)
        if len(self.slug) == 0: 
            self.slug = f'{slugify(self.title)}-{self.id}'
        super(self).save(*args, **kwargs)


