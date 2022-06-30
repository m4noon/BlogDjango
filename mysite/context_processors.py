from category.models import Category
from blog.models import Post
from tag.models import Tag


def categories(request):
    categories = Category.objects.all
    return {'categories': categories}


def posts(request):
    posts = Post.objects.all()[:5]
    return {'posts': posts}


def tags(request):
    tags = Tag.objects.all()
    return {'tags': tags}
