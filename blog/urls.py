from django.urls import path , include 
from .views import BlogDetailView, BlogView

app_name = 'blog'

urlpatterns = [
    path('',BlogView.as_view(),name='blog'),
    path('blog-detail/<int:pk>', BlogDetailView.as_view(), name="blog-details"),
    path('category/<str:category>', BlogView.as_view(), name="blogs_category"),
    path('tag/<str:tag>', BlogView.as_view(), name="blogs_tag"),
    path('api/v1/', include("blog.api.v1.urls")),
]