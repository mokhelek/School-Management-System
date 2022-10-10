from django.shortcuts import render, get_object_or_404, redirect
from .models import TeacherInfo
from django.contrib.auth.models import User 
from .forms import CreateTeacher
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import SignUpForm , SessionForm
from django.contrib.auth import login
from students.models import *
# Create your views here.
def teacher_list(request):
    teachers = TeacherInfo.objects.all()

    paginator = Paginator(teachers, 10)
    page = request.GET.get('page')
    paged_teachers = paginator.get_page(page)
    context = {
        "teachers": paged_teachers
    }
    return render(request, "teachers/teacher_list.html", context)


def single_teacher(request, teacher_id):
    single_teacher = get_object_or_404(TeacherInfo, pk=teacher_id)
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
        "single_teacher": single_teacher,
          "logged_in_as_student":logged_in_as_student,
        "logged_in_as_teacher": logged_in_as_teacher,
        "students":students,
        "teachers":teachers
    }
    return render(request, "teachers/single_teacher.html", context)


def create_teacher(request):
    if request.method == "POST":
        forms = CreateTeacher(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Teacher Registration Successfully!")
        return redirect("teachers:teacher_list")
    else:
        forms = CreateTeacher()

    context = {
        "forms": forms
    }
    return render(request, "teachers/create_teacher.html", context)


def edit_teacher(request, pk):
    teacher_edit = TeacherInfo.objects.get(id=pk)
    edit_teacher_forms = CreateTeacher(instance=teacher_edit)

    if request.method == "POST":
        edit_teacher_forms = CreateTeacher(request.POST, request.FILES or None, instance=teacher_edit)

        if edit_teacher_forms.is_valid():
            edit_teacher_forms.save()
            messages.success(request, "Edit Teacher Info Successfully!")
            return redirect("teachers:teacher_list")

    context = {
        "edit_teacher_forms": edit_teacher_forms
    }
    return render(request, "teachers/edit_teacher.html", context)


def delete_teacher(request, teacher_id):
    teacher_delete = TeacherInfo.objects.get(id=teacher_id)
    teacher_delete.delete()
    messages.success(request, "Delete Teacher Info Successfully")
    return redirect("lecturers:teacher_list")


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
            print(users)
            studentProfiles = TeacherInfo.objects.create( name = users , teacher_email=users.email,full_name=users.get_full_name())
            studentProfiles.save()

            new_user.save()
          
            login(request, new_user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'teachers/registration/register.html', context)


def session(request):
    if request.method == "POST":
        form = SessionForm(request.POST)

        if form.is_valid():
            form.save()
        messages.success(request, "Session created Successfully!")
        return redirect("home")
    else:
        form = SessionForm()

    context = {'form': form}
    return render(request, "teachers/session.html" , context  )

def single_session(request, session_id):
    session = StudentSession.objects.get(id=session_id)
    context = {"session":session}
    return render(request,"teachers/single_session.html",context)