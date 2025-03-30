from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from portfolio.models import Portfolio
from .serializer import PortfolioSerializer

class PortfolioListCreateView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
