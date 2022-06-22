from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from .models import Post
from django.template import loader


def index(request):
    return HttpResponse("Hello, <h1 > HO HO HO </h1> world. You're at the polls index.")


def show_all_posts(request):
    all_posts = Post.objects.order_by('-publish')[:5]
    template = loader.get_template('blogs/show_all_posts.html')
    context = {
        'all_posts': all_posts,
    }
    return HttpResponse(template.render(context, request))


def show_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blogs/show_post.html', {'post': post})

