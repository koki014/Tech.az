
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from django.conf import settings
from .models import Articles
from tech.commons import slugify

print('salam')
@receiver(pre_save, sender=Articles)
def create_product(sender, instance, **kwargs):
    queryset = Articles.objects.filter(title=instance.title).first()
    if not queryset:
        instance.slug = f'{slugify(instance.title)}'
        print(queryset, 'sasasasa')
    else:
        print(queryset, 'aaaaaaaaaa')

        instance.slug = f'{slugify(instance.title)}-{queryset.id}'
    instance.file_abs_url = f'{settings.SITE_ADDRESS}/api/articles/{instance.slug}/'