from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


def index(request):
    all_posts = Post.objects.order_by('-publish')[:5]
    return render(request, 'post/index.html', {'all_posts': all_posts,})


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'post/detail.html', {'post': post})


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/new.html'
    fields = ['title', 'slug', 'body', 'status']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/edit.html'
    fields = ['title', 'body', 'status']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('index')

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