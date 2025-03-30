from django.db import models
from portfolio.models import Portfolio
from accounts.models import User,Profile

# Create your models here.


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE, related_name="order")
    is_paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    zarinpal_authority=models.CharField(max_length=100, blank=True, null=True)
    zarinpal_refid=models.CharField(max_length=100, blank=True, null=True)
    zarinpal_data=models.TextField(blank=True, null=True)


    @property
    def phone(self):
        return self.profile.phone if self.profile else None
    
    @property
    def address(self):
        return self.profile.address if self.profile else None
    
    @property
    def postal_code(self):
        return self.profile.postal_code

    def __str__(self):
        return f"Order {self.id}"
    
    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price * item.quantity
        return total

    def __iter__(self):
        for item in self.items.all():
            yield item


class Order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"