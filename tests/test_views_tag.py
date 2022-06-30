from django.test import TestCase
from tag.models import Tag


class TagViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='new')

    def test_200(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')
