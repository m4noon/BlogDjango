from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from category.models import Category
from tag.models import Tag


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', height_field=None, default='std_img.jpg')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', args=[str(self.id)])
