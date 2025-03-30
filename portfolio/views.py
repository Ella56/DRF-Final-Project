from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio

# Create your views here.
class PortfolioView(ListView):
   model = Portfolio
   template_name = 'portfolio/portfolio.html'
   context_object_name = 'portfolio'
   def get_queryset(self):
        if self.kwargs.get("category"):
            protfolios = self.model.objects.filter(category__title=self.kwargs.get("category"), status=True)
        elif self.kwargs.get("name"):
            protfolios = Portfolio.objects.filter(creator__user__email=self.kwargs.get("name"), status=True)
        elif self.request.GET.get("search"):
            search = self.request.GET.get("search")
            protfolios = self.model.objects.filter(content__contains=search, status=True)
        else:
            protfolios = Portfolio.objects.filter(status=True)
        return protfolios
   
class PortfolioDetailsView(DetailView):
   model = Portfolio
   template_name = 'portfolio/portfolio-details.html'
