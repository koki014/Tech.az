from django.db.models.signals import post_save, pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from django.conf import settings
from .models import News
from tech.commons import slugify


@receiver(post_save, sender=News)
def create_product(sender, instance, created,  **kwargs):
    if created:
        instance.slug = f'{slugify(instance.title)}-{instance.id}'
        instance.file_abs_url = f'{settings.SITE_ADDRESS}/api/articles/{instance.slug}/'
        instance.save()