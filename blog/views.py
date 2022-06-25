from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView

from .models import Category
from .models import Post
from .models import Tag


def index(request):
    all_posts = Post.objects.order_by('-publish')[:5]
    return render(request, 'blog/show_all_posts.html', {'all_posts': all_posts,})


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/show_post.html', {'post': post})

"""
CRUD for Post
CRUD for Tags
CRUD for Category
CRUD for Comments
(
Create Read(get) Update Delete
Read -> (Index, detail(:id))
)
User - auth (sign in, sign up, password reset)
Policy - current_user: manager user admin, anonimous_user
"""