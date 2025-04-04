from django.db import models
from root.models import Team, Client,Testimonials

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title=models.CharField(max_length=100)
    image1=models.ImageField(upload_to="portfolio",default="default.jpg")
    image2=models.ImageField(upload_to="portfolio",default="default.jpg")
    image3=models.ImageField(upload_to="portfolio",default="default.jpg")
    image4=models.ImageField(upload_to="portfolio",default="default.jpg")
    content_one=models.TextField()
    testimonial=models.ForeignKey(Testimonials,on_delete=models.CASCADE, related_name='portfolio')
    content_two=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    project_data=models.DateField(auto_now_add=True)
    price=models.PositiveIntegerField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def truncate_chars(self):
        return self.content_one[:30]
    
