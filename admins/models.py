from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class AdminInfo(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE ,default=1 )
    full_name = models.CharField(max_length=100 ,null=True,blank=True )
    admin_email = models.EmailField(unique=True ,null=True,blank=True)
    admin_cellphone = models.CharField(max_length=100 ,null=True,blank=True )
   
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10) 

    def __str__(self):
        return str(self.full_name)
