from rest_framework import serializers
from blog.models import Blog, Comment, Subject, Tag, Blog_category, Author


class BlogSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source="subject.title", read_only=True)
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
    parent = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["blog", "name", "email", "website", "content", "parent", "created_at", "status"]
        read_only_fields = ["blog", "parent", "created_at", "status"]

    def get_parent(self, instance):
        return instance.parent.id if instance.parent else None

    def get_status(self, instance):
        return "Approved" if instance.status else "Pending"
