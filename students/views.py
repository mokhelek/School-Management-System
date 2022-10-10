from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import login
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import CreateStudent
from django.contrib.auth.models import User 

#from .models import StudentProfile
from .forms import SignUpForm
# Create your views here.
def student_list(request):
    students = StudentInfo.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)
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

    context = {
        "students": paged_students,
           "logged_in_as_student":logged_in_as_student,
        "logged_in_as_teacher": logged_in_as_teacher,
        "students":students,
        "teachers":teachers
    }
    return render(request, "students/student_list.html", context)

def single_student(request, student_id):
    single_student = get_object_or_404(StudentInfo, pk=student_id)
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
            
    context = {
        "single_student": single_student,
        "logged_in_as_student":logged_in_as_student,
        "logged_in_as_teacher": logged_in_as_teacher,
        "students":students,
        "teachers":teachers
    }
    return render(request, "students/student_details.html", context)

def student_regi(request):
    if request.method != 'POST':
        
        form = SignUpForm()
    else:
        
       
                    
            form = SignUpForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                get_id = form.instance.id  # get the id of a use--it has a username inside
                users = User.objects.get(id=get_id) # get the new user
                studentProfiles = StudentInfo.objects.create( name = users, full_name=users.get_full_name() ,student_email = users.email)
                studentProfiles.save()

                new_user.save()
        
                login(request, new_user)
                return redirect('home')
            
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
                
    context = {'form': form,   
                        "logged_in_as_student":logged_in_as_student,
                        "logged_in_as_teacher": logged_in_as_teacher,
                        "students":students,
                        "teachers":teachers}
    return render(request, 'students/register.html', context)    
 
           
    


   
def edit_student(request, pk):
    student_edit = StudentInfo.objects.get(id=pk)
    edit_forms = CreateStudent(instance=student_edit)
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
            
    if request.method == "POST":
        #edit_forms = CreateStudent(request.POST, instance=student_edit)
        edit_forms = CreateStudent(instance=student_edit, data=request.POST)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Edit Student Info Successfully!")
            if logged_in_as_student:
                return redirect("home")
            else:
                return redirect("students:student_list")

    context = {
        "edit_forms": edit_forms,
         "logged_in_as_student":logged_in_as_student,
        "logged_in_as_teacher": logged_in_as_teacher,
        "students":students,
        "teachers":teachers
    
    }
    return render(request, "students/edit_student.html", context)

def delete_student(request, student_id):
    student_delete = StudentInfo.objects.get(id=student_id)
    student_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("students:student_list")

def attendance_count(request):
    class_name = request.GET.get("class_name", None)
    if class_name:
        student_list = StudentInfo.objects.filter(class_type__class_short_form=class_name)
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
                
        context = {
            "student_list": student_list,
            "logged_in_as_student":logged_in_as_student,
        "logged_in_as_teacher": logged_in_as_teacher,
        "students":students,
        "teachers":teachers
            
            }
    else:
        context = {}
    return render(request, "students/attendance_count.html", context)



def register(request):

    
    if request.method != 'POST':
        # Display blank registration form. 
        form = SignUpForm()
    else:
        # Process completed form.
        form = SignUpForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            get_id = form.instance.id  # get the id of a use--it has a username inside
            users = User.objects.get(id=get_id) # get the new user
            print(users.email)
            print(users)
            studentProfiles = StudentInfo.objects.create( name = users, full_name=users.get_full_name() ,student_email = users.email)
            studentProfiles.save()

            new_user.save()
            login(request, new_user)
            return redirect('home')
            
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
        context = {
            'form': form,
            "logged_in_as_student":logged_in_as_student,
            "logged_in_as_teacher": logged_in_as_teacher,
            "students":students,
            "teachers":teachers               
                    }
                

    context = { 'form': form,}
             
      
    return render(request, 'students/registration/register.html', context)














                
"""           
if logged_in_as_student in students:
                login(request, new_user)
                return redirect('home')
            
            elif logged_in_as_teacher:
                login(request, new_user)
                return redirect('home')
            else:
                return redirect('home')
   
        """