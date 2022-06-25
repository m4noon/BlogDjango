from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView


def index(request):
    return HttpResponse("Index page")
