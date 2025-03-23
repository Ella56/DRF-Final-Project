from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio

# Create your views here.
class PortfolioView(ListView):
   pass

class PortfolioDetailsView(DetailView):
    pass
