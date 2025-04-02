from django.urls import path
from .views import *

app_name = "payment"

urlpatterns = [
    path('request/' , PaymentRequestView.as_view() , name='request'),
    path('verify/' , PaymentVerifyView.as_view() , name='verify'),
]