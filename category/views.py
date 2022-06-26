from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/index.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        posts = Post.objects.filter(category=category.pk)
        context["posts"] = posts
        return context


class CategoryCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = u"manager"
    model = Category
    template_name = 'category/new.html'
    fields = ['name']


class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = u"manager"
    model = Category
    template_name = 'category/edit.html'
    fields = ['name']


class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = u"manager"
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category:index')
