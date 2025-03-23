from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'root/index.html'


class AboutView(TemplateView):
    pass


class ContactView(FormView):
    pass

class TestimonialView(TemplateView):
    pass
