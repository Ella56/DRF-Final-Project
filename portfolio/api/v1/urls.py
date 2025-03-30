from django.urls import path
from .views import PortfolioListCreateView, PortfolioDetailView

urlpatterns = [
    path('', PortfolioListCreateView.as_view(), name='portfolio-list'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]
