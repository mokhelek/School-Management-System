from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class TeacherDeptInfo(models.Model):
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name

class TeacherSubInfo(models.Model):
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name

class TeacherInfo(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE ,default=1 ) # this has the username inside
    email = models.EmailField(unique=True ,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10) 
    #teacher_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #passing_year = models.CharField(max_length=100)
    joining_date = models.DateField(auto_now_add=True)
    dept_type = models.ForeignKey(TeacherDeptInfo, on_delete=models.CASCADE ,null=True)
    sub_type = models.ForeignKey(TeacherSubInfo, on_delete=models.CASCADE,null=True)
    #salary = models.IntegerField()

    def __str__(self):
        return str(self.name)

