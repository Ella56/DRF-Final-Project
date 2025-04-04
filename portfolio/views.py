from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Portfolio, Category,Client

# Create your views here.
class PortfolioView(ListView):
   model = Portfolio
   template_name = 'portfolio/portfolio.html'
   context_object_name = 'portfolios'
   def get_queryset(self):
        if self.kwargs.get("category"):
            portfolios = self.model.objects.filter(category__title=self.kwargs.get("category"), status=True)
        else:
            portfolios = Portfolio.objects.filter(status=True)
        return portfolios
   
   
class PortfolioDetailsView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio-details.html'
    context_object_name= "portfolio"

    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        portfolio = get_object_or_404(Portfolio, id=id)
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.filter(status=True)
        context["client"] = Client.objects.filter(status=True)
        return context


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

