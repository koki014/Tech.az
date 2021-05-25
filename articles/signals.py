
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from .models import Articles
from tech.commons import slugify


@receiver(post_save, sender=Articles)
def create_product(sender, instance, **kwargs):
    queryset = Articles.objects.filter(title=instance.title)
    if not queryset:
        instance.slug = f'{slugify(instance.title)}'
        print(queryset, 'sasasasa')
    else:
        print(queryset, 'aaaaaaaaaa')

        instance.slug = f'{slugify(instance.title)} {queryset.id}'