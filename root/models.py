from django.db import models

# Create your models here.

class About(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="about",default="default.jpg")
    content_one=models.TextField()
    content_two=models.TextField()
    video=models.URLField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=100) 
    email=models.EmailField()   
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    image=models.ImageField(upload_to="team",default="default.jpg")
    name=models.CharField(max_length=100)
    job_position=models.TextField()
    x_pllatform=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    linkdin=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Client(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="client",default="default.jpg")
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

   

class Star(models.Model):
    count = models.IntegerField(default=5)

    def __str__(self):
        return str(self.count)

class Testimonials(models.Model):
     name=models.CharField(max_length=100)
     job=models.CharField(max_length=100)
     image=models.ImageField(upload_to="testimonials",default="default.jpg")
     stars=models.ForeignKey(Star,on_delete=models.CASCADE)
     content=models.TextField()
     status=models.BooleanField(default=True)
    

     def __str__(self):
        return self.name
    
     def stars_count(self):
        return range(self.stars.count)

