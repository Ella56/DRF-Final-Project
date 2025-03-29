from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from .models import Team, Client

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

class TestimonialView(TemplateView):
    pass
