from secrets import choice
from django.db import models
from django.contrib.auth.models import User 
from lecturers.models import TeacherInfo
# Create your models here.


class StudentModules(models.Model):
    module_name = models.CharField(max_length=80 , null=True , blank=True)
    module_description = models.CharField(max_length=200 , null=True , blank=True)
    #module_instructor = models.ForeignKey(TeacherInfo, on_delete=models.SET_NULL, null=True )
   
    def __str__(self):
        return self.module_name
       

class StudentInfo(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE ,default=1 ) 
    full_name = models.CharField(max_length=100 ,null=True,blank=True )
    student_number = models.CharField(max_length=50, unique=True,null=True,blank=True)
    student_email = models.EmailField(null=True,blank=True)
    student_cellphone = models.CharField(max_length=100 ,null=True,blank=True )
    faculty_choice = (
        ("Education", "Education"),
        ("Enginnering", "Enginnering"),
         ("Law", "Law"),
          ("Humanities", "Humanities"),
           ("Arts", "Arts"),
            ("Sciences", "Sciences"),
            ("Health Science", "Health Sciences")
    )
    Faculty = models.CharField( choices=faculty_choice, max_length=100 ,null=True,blank=True )
    
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    modules = models.ManyToManyField(StudentModules,related_name="modules", blank=True)
    
    def __str__(self):
        return str(self.full_name)


class Venues(models.Model):
    venue_name = models.CharField(max_length=255) 
    def __str__(self):
        return self.venue_name

class StudentSession(models.Model):
    session_name = models.CharField(max_length=100, null=True , blank=True)
    session_description = models.TextField(null=True , blank=True)
    session_date= models.DateField(null=True , blank=True)
    session_time = models.TimeField( null=True , blank=True)
    session_venue = models.ForeignKey(Venues, on_delete=models.CASCADE ,default="No Instructor Yet")
    module = models.ForeignKey(StudentModules, on_delete=models.CASCADE ,null=True , blank =True)
    
    date_added = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    
    def __str__(self):
        return f'{self.session_name}  @  {self.session_time}'
    
class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    session = models.ForeignKey( StudentSession, on_delete=models.CASCADE )
    time = models.TimeField(auto_now_add=True , null=True , blank=True)
    
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.student.full_name
    
    