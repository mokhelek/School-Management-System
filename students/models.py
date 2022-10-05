from secrets import choice
from django.db import models
from django.contrib.auth.models import User 
from teachers.models import TeacherInfo
# Create your models here.


class Venues(models.Model):
    venue_name = models.CharField(max_length=255) 
    def __str__(self):
        return self.venue_name
     
class StudentSession(models.Model):
    session_name = models.CharField(max_length=100)
    session_date= models.DateField()
    session_time = models.TimeField()
    session_venue = models.ForeignKey(Venues, on_delete=models.CASCADE ,default="No Instructor Yet")
    def __str__(self):
        return self.section_name
    
class StudentModules(models.Model):
    module_name = models.CharField(max_length=80 , null=True , blank=True)
    module_description = models.CharField(max_length=200 , null=True , blank=True)
    #module_instructor = models.ForeignKey(TeacherInfo, on_delete=models.SET_NULL, null=True )
    session = models.ForeignKey(StudentSession, on_delete=models.CASCADE ,null=True , blank =True)
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


class AttendanceManager(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            class_type__class_short_form=student_class,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.admission_id
    
    