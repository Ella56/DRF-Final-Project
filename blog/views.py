from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogView(ListView):
    template_name = 'blog/blog.html'
    def get_queryset(self):
        if self.kwargs.get("category"):
            blogs= self.model.objects.filter(category__title=self.kwargs.get("category"), status=True)
        elif self.kwargs.get("name"):
            blogs = Blog.objects.filter(creator__user__email=self.kwargs.get("name"), status=True)
        elif self.request.GET.get("search"):
            search = self.request.GET.get("search")
            blogs = self.model.objects.filter(content__contains=search, status=True)
        else:
            blogs = Blog.objects.filter(status=True)#
        return blogs

class BlogDetailView(DetailView):
    template_name = 'blog/blog-details.html'