from rest_framework import serializers
from blog.models import Blog, Comment, Tag, Blog_category, Author


class BlogSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source="category.name", read_only=True)
    author = serializers.CharField(source="author.name", read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = "__all__"

    def get_tags(self, instance):
        return [tag.name for tag in instance.tag.all()]


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.CharField(source="blog.title", read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["blog", "name", "email", "website", "content", "created_at","updated_at", "status"]
        read_only_fields = ["blog", "parent", "created_at","updated_at", "status"]


    def get_status(self, instance):
        return "Approved" if instance.status else "Pending"
