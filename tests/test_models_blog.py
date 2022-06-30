from django.test import TestCase
from blog.models import Post


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='News', body='something')

    def test_title(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_body(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('body').verbose_name
        self.assertEquals(field_label, 'body')

    def test_tags(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('tags').verbose_name
        self.assertEquals(field_label, 'tags')

    def test_publish(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('publish').verbose_name
        self.assertEquals(field_label, 'publish')

    def test_created(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'created')

    def test_updated(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('updated').verbose_name
        self.assertEquals(field_label, 'updated')

    def test_status(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_category(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_image(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)

    def test_str(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEquals(expected_object_name, str(post))

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/post/1/')
