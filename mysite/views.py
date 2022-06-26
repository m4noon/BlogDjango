from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.views.generic import ListView
from category.models import Category
from blog.models import Post


def index(request):
    template = 'index.html'
    categories_with_posts = dict()
    for category in Category.objects.all():
        posts = Post.objects.filter(category=category.pk).order_by('-created')[:5]
        if posts:
            categories_with_posts[category] = posts
    context = {
        "categories_with_posts": categories_with_posts,
    }
    return render(request, template, context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
