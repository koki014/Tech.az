from django.db import models
from django.contrib.auth import get_user_model
from main.models import Tag
User = get_user_model()


class Video(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Tag)

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Basliq", max_length=256)
    content = models.TextField('Mezmun')
    image = models.ImageField("Image", upload_to='video_images')
    cover_image = models.ImageField("Image", upload_to='cover_images', null=True, blank=True)
    video_link = models.URLField(max_length=300, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

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
