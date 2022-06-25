from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'tag/index.html'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag/detail.html'


class TagCreateView(CreateView):
    model = Tag
    template_name = 'tag/new.html'
    fields = ['name']


class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'tag/edit.html'
    fields = ['name']


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag/delete.html'
    success_url = reverse_lazy('tag:index')