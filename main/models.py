from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class Join(models.Model):
    first_name = models.CharField(_('Name'), max_length=30, db_index=True)
    last_name = models.CharField(_('Surname'), max_length=50, db_index=True)
    email = models.EmailField(_('email address'), unique=True)

    # moderations
    is_published = models.BooleanField(_('is published'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Join')
        verbose_name_plural = _('Joins')
        # ordering = ('-created_at')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    title = models.CharField(_('Title'), max_length=100, db_index=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title