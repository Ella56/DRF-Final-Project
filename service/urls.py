from django.urls import path, include
from django.urls import path , include
from .views import ServiceDetailView, ServiceView

app_name = 'service'

urlpatterns = [
    path("", ServiceView.as_view(),name="service"),
    path("service-details/<int:pk>", ServiceDetailView.as_view(), name="service-details"),
    path("api/v1/", include("service.api.v1.urls")),

]