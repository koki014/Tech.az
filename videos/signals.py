
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from django.conf import settings
from .models import Video
from tech.commons import slugify

@receiver(pre_save, sender=Video)
def create_product(sender, instance, **kwargs):
    queryset = Video.objects.filter(title=instance.title).first()
    if not queryset:
        instance.slug = f'{slugify(instance.title)}'
    else:
        instance.slug = f'{slugify(instance.title)}-{queryset.id}'
    instance.file_abs_url = f'{settings.SITE_ADDRESS}/api/videos/{instance.slug}/'