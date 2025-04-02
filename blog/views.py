from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,Comment, Blog_category, Tag
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = "blogs"
    paginate_by = 1
    
    def get_queryset(self):
        if self.kwargs.get("category"):
            blogs = self.model.objects.filter(category__title=self.kwargs.get("category"))
        elif self.kwargs.get("tag"):
            blogs = self.model.objects.filter(tag__title=self.kwargs.get("tag"))
            # elif self.kwargs.get("name"):
            #blogs = Blog.objects.filter(creator__user__email=self.kwargs.get("name"), status=True)
        elif self.request.GET.get('search') is not None:
            search = self.request.GET.get('search')
            blogs = Blog.objects.filter(desc1__contains = search)
        else:
            blogs = Blog.objects.filter(status=True).order_by('-created_at')
        return blogs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Blog_category.objects.filter(status=True)
        context['tag'] = Tag.objects.filter(status=True)
        first = 1
        blogs_paginate = Paginator(self.get_queryset(), 2)
        last = blogs_paginate.num_pages
        context['first'] = first
        context['last'] = last
        
        
        return context
    




class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.filter(status=True, blog=Blog.id)
        context["blogs"] = Blog.objects.filter(status=True).order_by("-created_at")[:5]
        return context
    

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                id = self.kwargs["pk"]
                blog = get_object_or_404(Blog, id=id)
                comment = form.save(commit=False)
                comment.blog = blog
                comment.name = request.user
                parent_id = request.POST.get("parent_id") #check if its reply
                if parent_id:
                    parent_comment = get_object_or_404(Comment, id= parent_id)
                    comment.parent = parent_comment # set parent if its reply
                comment.save()
                messages.add_message(self.request, messages.SUCCESS, "Your comments has been successfully sent ")
                return redirect(self.request.path_info, pk=blog.pk)
            else:
                messages.add_message(request, messages.ERROR, "invalid data")
                return redirect(self.request.path_info)
        else:
            return redirect("accounts:login")