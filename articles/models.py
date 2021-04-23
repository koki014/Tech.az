from django.db import models
from django.contrib.auth import get_user_model
from main.models import Tag
User = get_user_model()

# Create your models here.

class Articles(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Basliq", max_length=256)
    content = models.TextField('Mezmun')
    views = models.PositiveIntegerField(default=0)

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


