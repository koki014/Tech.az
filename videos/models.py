from django.db import models
from django.contrib.auth import get_user_model
from main.models import Tag
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from tech.commons import slugify

User = get_user_model()


class Video(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Qisa mezmun", max_length=256)
    content = models.TextField('Mezmun')
    image = models.ImageField("Image", upload_to='video_images')
    cover_image = models.ImageField("Cover Image", upload_to='cover_images')
    video_link = models.URLField(max_length=300)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)
    file_abs_url = models.URLField(_("abs url"), default='', max_length=200)


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        videos = Video.objects.filter(title=self.title).first()
        if not videos: 
            self.slug = slugify(f'{self.title}')
        else:
            print('girmedi')
            self.slug = f'{slugify(self.title)}-{self.id}'
        self.file_abs_url = f'{settings.SITE_ADDRESS}/videos/{self.slug}/'
        super(Video, self).save(*args, **kwargs)



