from django.test import TestCase
from blog.models import Post


class BlogViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='News', body='something')

    def test_200(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')