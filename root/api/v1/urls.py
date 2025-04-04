from django.urls import path , include
from .views import (
    AboutViewSet, ContactViewSet, TeamViewSet,
    ClientViewSet, StarViewSet, TestimonialsViewSet , APIHomeView
)


urlpatterns = [
    path("", APIHomeView.as_view(), name="api-home"),

    path('about/', AboutViewSet.as_view({"get": "list", "post": "create"}), name="about-list"),
    path('about/<int:pk>/', AboutViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="about-detail"),

    path('contact/', ContactViewSet.as_view({"get": "list", "post": "create"}), name="contact-list"),
    path('contact/<int:pk>/', ContactViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="contact-detail"),

    path('team/', TeamViewSet.as_view({"get": "list", "post": "create"}), name="team-list"),
    path('team/<int:pk>/', TeamViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="team-detail"),

    path('client/', ClientViewSet.as_view({"get": "list", "post": "create"}), name="client-list"),
    path('client/<int:pk>/', ClientViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="client-detail"),

    path('star/', StarViewSet.as_view({"get": "list", "post": "create"}), name="star-list"),
    path('star/<int:pk>/', StarViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="star-detail"),

    path('testimonials/', TestimonialsViewSet.as_view({"get": "list", "post": "create"}), name="testimonials-list"),
    path('testimonials/<int:pk>/', TestimonialsViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="testimonials-detail"),
]

