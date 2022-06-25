from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from category.models import Category

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/new.html'
    fields = ['title', 'slug', 'body', 'status', 'category', 'tags']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/edit.html'
    fields = ['title', 'body', 'status', 'category', 'tags']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post:index')

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