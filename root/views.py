from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import Team, Client, Testimonials

# Create your views here.
class HomeView(TemplateView):
    template_name = 'root/index.html'


class AboutView(TemplateView):
    template_name = 'root/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(status=True)[:4]
        context["clients"] = Client.objects.filter(status=True)

        return context


class ContactView(FormView):
    pass

class TestimonialView(ListView):
    model = Testimonials
    template_name = 'root/testimonials.html'
    context_object_name = "testimonials"
    paginate_by = 2

    def get_queryset(self):
        testimonials = self.model.objects.filter(status=True)
        return testimonials
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first = 1
        blogs_paginate = Paginator(self.get_queryset(), 2)
        last = blogs_paginate.num_pages
        context["first"] = first
        context["last"] = last
        
        return context
