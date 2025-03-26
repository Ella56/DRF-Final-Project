from django.db import models
from portfolio.models import Category

# Create your models here.


class Special_services(models.Model):
    title=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Service(models.Model):
    title=models.CharField(max_length=100)
    content_one=models.TextField()
    content_two=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content_three=models.TextField()
    specials=models.ManyToManyField(Special_services)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.title


