from lecturers.models import *
from students.models import *
from admins.models import *


def user_authentication(request):
    if request.user.is_authenticated:
        students = StudentInfo.objects.all()
        teachers=TeacherInfo.objects.all()
        admins = AdminInfo.objects.all()
        
        try:
            logged_in_as_student = StudentInfo.objects.get(name= request.user)
        except:
            logged_in_as_student = ""
           
            
        try:
            logged_in_as_teacher = TeacherInfo.objects.get(name= request.user)
        except:
            logged_in_as_teacher=""
        
        try:
            logged_in_as_admin = AdminInfo.objects.get(name= request.user)
        except:
            logged_in_as_admin = ""
        
        
        return {
            "students":students, 
            "logged_in_as_student":logged_in_as_student,
            "logged_in_as_teacher":logged_in_as_teacher,
            "teachers":teachers,
            "admins":admins,
            "logged_in_as_admin":logged_in_as_admin,
           }
    
    else:
        return {}
