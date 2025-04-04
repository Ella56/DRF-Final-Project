
from service.models import Service
from .forms import CheckoutForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order_item , Order
from django.views.generic import FormView
from django.shortcuts import render , redirect
from portfolio.models import Portfolio
from accounts.models import Profile
# Create your views here.

#@login_required
def cart_view(request):
    portfolio_list = []
    cart = request.session.get('cart', {})
    for id , quantity in cart.items():
        try:
            portfolio = Portfolio.objects.get(id=int(id))
            quantity = int(quantity)
            portfolio_list.append({"portfolio" : portfolio ,
                                    "quantity" : quantity ,
                                    "total_price" : portfolio.price * quantity})
            total = 0
            for item in portfolio_list:
                total += item['total_price']
        except Portfolio.DoesNotExist:
           pass
    context = {
        "portfolio_list" : portfolio_list,
        "total" : total,
    }
    return render(request , 'cart/cart.html',context=context)


class CheckoutView(LoginRequiredMixin , FormView):
    template_name = 'cart/checkout.html'
    form_class = CheckoutForm

    def form_valid(self, form):
        user = self.request.user
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']
        postal_code = form.cleaned_data['postal_code']
        profile = Profile.objects.create(user=user , phone=phone , address=address , postal_code=postal_code)
        order = Order.objects.create(user=user,profile=profile)
        cart = self.request.session.get('cart', {})
        for id , quantity in cart.items():
            portfolio = Portfolio.objects.get(id=int(id))
            quantity = int(quantity)
            Order_item.objects.create(order=order , product=portfolio , price=portfolio.price , quantity=quantity)

        payment = self.request.session.get("payment" , {})
        payment["order_id"] = order.id
        payment["total_price"] = order.total_price()
        self.request.session["payment"] = payment
        self.request.session.modified = True
        return redirect('payment:request')