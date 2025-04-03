from django.db import models
from accounts.models import Profile

# Create your models here.



class Tag(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=100)
    content=models.TextField()
    x_platform=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Blog_category(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)

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
    tag=models.ManyToManyField(Tag)
    category=models.ForeignKey(Blog_category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    def truncate_chars(self):
        return self.content_one[:100]

    def get_comments(self):
        return self.comments.filter(status=True)
    
    def comment_count(self):
        return self.comments.count()

    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website = models.URLField()
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name.user.email
    
    def get_replays(self):
        return self.replays.filter(status=True)
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replays', on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name.user.email
    