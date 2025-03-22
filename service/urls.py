from django.urls import path
from .views import service,service_detail
app_name = 'service'
urlpatterns = [
    path('',service,name='service'),
    path('service_detail',service_detail,name='service_detail'),
]