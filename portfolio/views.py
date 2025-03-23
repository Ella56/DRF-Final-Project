from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def portfolio(request):
    return render(request,'portfolio/portfolio.html')

def portfolio_details(request):
    return render(request,'portfolio/portfolio-details.htm')
