from django.db import models
from root.models import Team, Client

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,default="")
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title=models.CharField(max_length=100,default="")
    image1=models.ImageField(upload_to="portfolio",default="default.jpg")
    image2=models.ImageField(upload_to="portfolio",default="default.jpg")
    image3=models.ImageField(upload_to="portfolio",default="default.jpg")
    image4=models.ImageField(upload_to="portfolio",default="default.jpg")
    content_one=models.TextField(default="")
    quoto=models.TextField(default="")
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    content_two=models.TextField(default="")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    project_data=models.DateField(auto_now_add=True)
    price=models.PositiveIntegerField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
