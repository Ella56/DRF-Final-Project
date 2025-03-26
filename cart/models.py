from django.db import models
from portfolio.models import Portfolio
from accounts.models import User

# Create your models here.


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    zarinpal_authority=models.CharField(max_length=100,)
    zarinpal_refid=models.CharField(max_length=100)
    zarinpal_data=models.TextField()

    def __str__(self):
        return self.user

class Order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.product.title