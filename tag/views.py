from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from .models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'tag/index.html'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.get_object()
        posts = Post.objects.filter(tags=tag.pk)
        context["posts"] = posts
        return context


class TagCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Tag
    template_name = 'tag/new.html'
    fields = ['name']
    group_required = u"manager"


class TagUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Tag
    template_name = 'tag/edit.html'
    fields = ['name']
    group_required = u"manager"


class TagDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tag/delete.html'
    success_url = reverse_lazy('tag:index')
    group_required = u"manager"
