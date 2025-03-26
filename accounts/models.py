from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="profile",default="default.jpg")
    phone=models.CharField(max_length=100,)
    address=models.TextField(default="")
    postal_code=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
