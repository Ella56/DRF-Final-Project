from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,Comment, Blog_category, Tag
from django.views.generic import ListView, DetailView, FormView, CreateView
from .forms import ReplyForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from accounts.models import Profile

# Create your views here.


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = "blogs"
    paginate_by = 1
    
    def get_queryset(self):
        if self.kwargs.get("category"):
            blogs = self.model.objects.filter(category__name=self.kwargs.get("category"))
        elif self.kwargs.get("tag"):
            blogs = self.model.objects.filter(tag__name=self.kwargs.get("tag"))
            # elif self.kwargs.get("name"):
            #blogs = Blog.objects.filter(creator__user__email=self.kwargs.get("name"), status=True)
        elif self.request.GET.get("search"):
            search = self.request.GET.get("search")
            blogs = self.model.objects.filter(title_contains=search, status=True)
        else:
            blogs = Blog.objects.filter(status=True).order_by('-created_at')

        return blogs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Blog_category.objects.filter(status=True)
        context['tag'] = Tag.objects.filter(status=True)
        category_id= self.kwargs.get('category_id')
        if category_id:
            context['selected_category'] = Blog_category.objects.get(id=category_id)
        context['category_post_count'] = Blog.objects.filter(category_id=category_id).count()
        context['recent_posts'] = Blog.objects.filter(status=True).order_by("-created_at")[:5]

        first = 1
        blogs_paginate = Paginator(self.get_queryset(), 2)
        last = blogs_paginate.num_pages
        context['first'] = first
        context['last'] = last
        
        
        return context
    




class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog-details.html'

    # def get_queryset(self):
    #     if self.request.GET.get("search"):
    #         search = self.request.GET.get("search")
    #         blogs = self.model.objects.filter(title_contains=search, status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Blog_category.objects.filter(status=True)
        context['tag'] = Tag.objects.filter(status=True)
        category_id= self.kwargs.get('category_id')
        if category_id:
            context['selected_category'] = Blog_category.objects.get(id=category_id)
        context['category_post_count'] = Blog.objects.filter(category_id=category_id).count()
        context['form'] = CommentForm
        blog = get_object_or_404(Blog, id=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(status=True, blog=blog.id)
        context['recent_posts'] = Blog.objects.filter(status=True).order_by("-created_at")[:5]
        return context
    

    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if request.user.is_authenticated:
    #         if form.is_valid():
    #             id = self.kwargs["pk"]
    #             blog = get_object_or_404(Blog, id=id)
    #             comment = form.save(commit=False)
    #             comment.blog = blog
    #             comment.name = request.user
    #             parent_id = request.POST.get("parent_id") #check if its reply
    #             if parent_id:
    #                 try:
    #                     parent_id = int(parent_id)
    #                     parent_comment = get_object_or_404(Comment, id= parent_id)
    #                     comment.parent = parent_comment # set parent if its reply
    #                 except ValueError:
    #                     messages.add_message(request, messages.ERROR, "invalid parent id")
                        
    #                 comment.save()
    #                 messages.add_message(self.request, messages.SUCCESS, "Your comments has been successfully sent ")
    #                 return redirect(self.request.path_info, pk=blog.pk)
    #             else:
    #                 messages.add_message(request, messages.ERROR, "invalid parent iid")
    #                 return redirect(self.request.path_info)

    #         else:
    #             print(form.errors)
    #             messages.add_message(request, messages.ERROR, "invalid data")
    #             return redirect(self.request.path_info)
    #     else:
    #         return redirect("accounts:login/signup")


class ReplyView(FormView):
    form_class = ReplyForm

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        return redirect('blog:blog-details', pk=comment.blog.pk)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        user = request.user
        email = user.email
        profile = Profile.objects.get(user=user)
        form = self.get_form()
        if form.is_valid():
            replay = form.save(commit=False)
            replay.comment = comment
            replay.name = profile
            replay.email = email
            replay.save()
            messages.success(request, 'Your reply has been successfully sent')
            return redirect('blog:blog-details', pk=comment.blog.pk)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, 'invalid Data')
        return super().form_invalid(form)


class CommentView(CreateView):
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
        return redirect(f'blog/blog-detail/{blog.pk}')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
        user = request.user
        email = user.email
        profile = Profile.objects.get(user=user)
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.name = profile
            comment.email = email
            comment.save()
            messages.success(request, 'Your comments has been successfully sent ')
            return redirect('blog:blog-detail', pk=blog.pk)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, 'invalid Data')
        return super().form_invalid(form)