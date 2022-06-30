from django.test import TestCase
from category.models import Category


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Social')

    def test_category(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название категории')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/category/1/')
