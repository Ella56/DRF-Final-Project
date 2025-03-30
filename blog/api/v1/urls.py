from django.urls import path
from .views import BlogViewSet, CommentViewSet

urlpatterns = [
    path('',BlogViewSet.as_view({"get": "list", "post": "create"}), name="blog-list"),
    path("<int:pk>/",BlogViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="blog-detail"),

    path("comments/", CommentViewSet.as_view({"get": "list", "post": "create"}), name="comment-list"),
    path("comments/<int:pk>/", CommentViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="comment-detail"),
]
