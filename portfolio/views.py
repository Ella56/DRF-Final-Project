from django.shortcuts import render, redirect
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

   def post(self , request , *args , **kwargs):
         
        cart = request.session.get("cart")
        if cart is None:
            request.session["cart"] = {}
            request.session.modified = True
            cart = request.session.get("cart")
        id = int(request.POST["product_id"])
        quantity = int(request.POST["quantity"])

        if id in cart:
              del cart[id]
              id = int(request.POST["product_id"])
              cart[id] = int(quantity)
              request.session.modified = True
        else :
              cart[id] = int(quantity)
              request.session.modified = True

        return redirect(request.path_info)

