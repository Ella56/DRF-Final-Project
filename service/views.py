from django.shortcuts import render, get_object_or_404 , redirect
from django.views.generic import ListView, DetailView
from .models import Service,Special_services,Category
# Create your views here.


class ServiceView(ListView):
    model=Service
    template_name="service/services.html"
    context_object_name = "services"


    def get_queryset(self):
        services = Service.objects.filter(status=True)

        return services
    


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



class ServiceDetailView(DetailView):
    model=Service
    template_name="service/service-details.html"
    context_object_name= "service"

    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        service = get_object_or_404(Service, id=id)
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.filter(status=True)
        context["specials"] = Special_services.objects.filter(status=True)
        return context