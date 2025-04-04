from django.urls import path , include
from .views import PortfolioView, PortfolioDetailsView

app_name = 'portfolio'

urlpatterns = [
    path("api/v1/", include("portfolio.api.v1.urls")),
    path('',PortfolioView.as_view(),name='portfolio'),
    path('portfolio-details/<int:pk>',PortfolioDetailsView.as_view(),name='portfolio-details'),
    path('category/<str:category>' ,PortfolioView.as_view(), name='portfolio-category' )

]