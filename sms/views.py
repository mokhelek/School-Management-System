from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import *
from teachers.models import *

@login_required
def index(request):
    if request.user.is_authenticated:
        students = StudentInfo.objects.all()
        teachers=TeacherInfo.objects.all()
        
        try:
            logged_in_as_student = StudentInfo.objects.get(name= request.user)
        except:
            logged_in_as_student = ""
           
            
        try:
            logged_in_as_teacher = TeacherInfo.objects.get(name= request.user)
        except:
            logged_in_as_teacher=""
            
            
        context = {"students":students, "logged_in_as_student":logged_in_as_student,"logged_in_as_teacher":logged_in_as_teacher,"teachers":teachers}
        return render(request, "home.html", context)
    
    
    else:
        logged_in_as_student = ""
        logged_in_as_teacher = ""
        context = {"students":students, "logged_in_as_student":logged_in_as_student,"logged_in_as_teacher":logged_in_as_teacher,"teachers":teachers}
        return render(request, "home.html", context)



