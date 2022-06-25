from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=64, db_index=True, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('tag:detail', args=[str(self.id)])