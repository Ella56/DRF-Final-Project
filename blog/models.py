from django.db import models

# Create your models here.


class Subject(models.Model):
    title=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=100)
    content=models.TextField()
    x_platform=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Blog_category(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image_one=models.ImageField(upload_to="blog",default="default.jpg")
    content_one=models.TextField(default="")
    tip=models.TextField(default="")
    content_two=models.TextField(default="")
    image_two=models.ImageField(upload_to="blog",default="default.jpg")
    mini_title=models.CharField(max_length=100)
    content_three=models.TextField(default="")
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)
    category=models.ForeignKey(Blog_category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    website=models.URLField()
    content=models.TextField(default="")
    parent=models.ForeignKey("self", on_delete=models.CASCADE,related_name="replies")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)


    def __str__(self):
        return f"Comment by {self.user} on {self.blog.title}"