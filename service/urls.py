from django.urls import path
from .views import ServiceDetailView, ServiceView

app_name = 'service'

urlpatterns = [
    path("", ServiceView.as_view(),name="service"),
    path("detail/<int:pk>", ServiceDetailView.as_view(), name="service-details")
]