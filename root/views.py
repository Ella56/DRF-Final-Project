from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from service.models import Service
from django.contrib import messages

# Create your views here.
class HomeView(TemplateView):
    template_name = 'root/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['services'] = Service.objects.filter(status=True)[:3]

        return context

class AboutView(TemplateView):
    template_name = "root/about.html"


def contact(request):
    if request.method == "POST":
        form =  ContactForm(request.POST)
        if request.user.is_authenticated and request.user.has_perm("sites.view_site"):
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "your contact received successfully")
                return render(request,"root/contact.html")
            else:
                messages.add_message(request, messages.ERROR, "your input data is not valid")
                return render(request,"root/contact.html")
        else:
            messages.add_message(request, messages.ERROR, "shoma dastresi haye lazem ro nadarid")
            return render(request,"root/contact.html")

    else:
        form = ContactForm()
        context = {'form': form}
        return render(request,"root/contact.html", context=context)


class TestimonialView(TemplateView):
    template_name = "root/testimonials.html"
