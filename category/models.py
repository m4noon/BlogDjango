from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category:detail', args=[str(self.id)])