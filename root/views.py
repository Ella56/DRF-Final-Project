from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.contrib import messages
from .models import Team, Client, Testimonials
from service.models import Service


# Create your views here.
class HomeView(TemplateView):
    template_name = 'root/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['services'] = Service.objects.filter(status=True)[:3]

        return context

class AboutView(TemplateView):

    template_name = 'root/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(status=True)[:4]
        context["clients"] = Client.objects.filter(status=True)

        return context


class ContactView(FormView):
    template_name = 'root/contact.html'
    form_class = ContactForm
    success_message = "Successfully sent message"
    error_message = "Data invalid"

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, self.error_message)
        return super().form_invalid(form)
    
    def get_success_url(self):
        return self.request.path  # Redirects back to the same page
    
    

class TestimonialView(ListView):
    model = Testimonials
    template_name = 'root/testimonials.html'
    context_object_name = "testimonials"
    paginate_by = 4

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


