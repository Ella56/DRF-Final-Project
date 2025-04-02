from portfolio.models import Category



def general_context(request):
    context = {
        "cart_items" : len(request.session.get("cart" , {})) 
    }
    return context