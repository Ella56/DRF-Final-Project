from django.urls import path
from .views import *


app_name = "api-services"

from .views import ServiceListCreateView, ServiceDetailView

urlpatterns = [
    path("", ServiceListCreateView.as_view(), name="service-list-create"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
]
