from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = u"manager"
    model = Post
    template_name = 'post/new.html'
    fields = ['title', 'body', 'image', 'status', 'category', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = u"manager"
    model = Post
    template_name = 'post/edit.html'
    fields = ['title', 'body', 'image', 'status', 'category', 'tags']


class PostDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = u"manager"
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