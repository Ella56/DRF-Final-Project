from django.urls import path
from .views import portfolio,portfolio_details
app_name = 'portfolio'
urlpatterns = [
    path('',portfolio,name='portfolio'),
    path('portfolio_details',portfolio_details,name='portfolio_details')
]