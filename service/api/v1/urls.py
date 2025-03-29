from django.urls import path
from .views import *


app_name = "api-services"

urlpatterns = [
    
    path("services/", ServiceView.as_view({"get" : "list", "post" : "create"}), name="all_services"),
    path("service-detail/<int:pk>/", ServiceView.as_view({"get" : "retrieve", "put" : "update", "patch" : "update", "delete" : "destroy"}), name="single_services"),

]