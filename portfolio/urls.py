from django.urls import path , include
from .views import PortfolioView, PortfolioDetailsView

app_name = 'portfolio'

urlpatterns = [
    path("api/v1/", include("portfolio.api.v1.urls")),

]