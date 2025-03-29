from django.urls import path, include
from .views import HomeView, ContactView, AboutView, TestimonialView

app_name = 'home'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about',AboutView.as_view(),name='about'),

]