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

    # def save(self, *args, **kwargs):

    #     videos = Video.objects.filter(title=self.title).first()
    #     if not videos: 
    #         self.slug = slugify(f'{self.title}')
    #     else:
    #         super().save(*args, **kwargs)
    #         self.slug = f'{slugify(self.title)}-{self.id}'
    #     self.file_abs_url = f'{settings.SITE_ADDRESS}/api/videos/{self.slug}/'
    #     super(Video, self).save(*args, **kwargs)



class VideosImage(models.Model):

    # relation's
    videos = models.ForeignKey("videos.Video", related_name='videos_images', on_delete=models.CASCADE, blank=True, null=True)

    # informations
    image = models.ImageField(_("Image"), upload_to='videos_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Video Şəkili'
        verbose_name_plural = 'Videonun Şəkilləri'
        ordering = ('-created_at',)



