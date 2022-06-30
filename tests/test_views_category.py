from django.test import TestCase
from category.models import Category


class CategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Social')

    def test_200(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')
