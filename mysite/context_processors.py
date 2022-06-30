from category.models import Category
from tag.models import Tag


def categories(request):
    categories = Category.objects.all
    return {'categories': categories}


def tags(request):
    tags = Tag.objects.all()
    return {'tags': tags}
