from django.urls import path
from .views import PortfolioView, PortfolioDetailsView

app_name = 'portfolio'

urlpatterns = [
    path('',PortfolioView.as_view(),name='portfolio'),
    path('details',PortfolioDetailsView.as_view(),name='portfolio-details'),
    path('category/<str:category>' ,PortfolioView.as_view(),name='portfolio-category' )
]