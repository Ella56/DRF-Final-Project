from django.urls import path , include 
from .views import BlogDetailView, BlogView, ReplyView,CommentView

app_name = 'blog'

urlpatterns = [
    path('',BlogView.as_view(),name='blog'),    
    path('category/<str:category>', BlogView.as_view(), name="blogs_category"),
    path('tag/<str:tag>', BlogView.as_view(), name="blogs_tag"),
    path('blog-detail/<int:pk>', BlogDetailView.as_view(), name="blog-details"),
    path('blog-detail/category/<str:category>', BlogView.as_view(), name="blogs_category"),
    path('blog-detail/tag/<str:tag>', BlogView.as_view(), name="blogs_tag"),
    path('blog-detail/add_reply/<int:pk>',ReplyView.as_view(), name='add_reply'),
    path('blog-detail/add_comments/<int:pk>',CommentView.as_view(), name='add_comment'),
    path('api/v1/', include("blog.api.v1.urls")),
]