from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogView(ListView):
    pass


class BlogDetailView(DetailView):
    pass