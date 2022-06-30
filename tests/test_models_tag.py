from django.test import TestCase
from tag.models import Tag


class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='new')

    def test_tag(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Тег')

    def test_get_absolute_url(self):
        tag = Tag.objects.get(id=1)
        self.assertEquals(tag.get_absolute_url(), '/tag/1/')
