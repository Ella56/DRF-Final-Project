from django.urls import path , include 
from .views import BlogDetailView, BlogView

app_name = 'blog'

urlpatterns = [
    path('',BlogView.as_view(),name='blog'),
    path('details',BlogDetailView.as_view(),name='blog-details'),
    path('api/v1/', include("blog.api.v1.urls")),
]