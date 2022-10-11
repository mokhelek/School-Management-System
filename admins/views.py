
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User 
from .models import *
from .forms import SignUpForm , CreateAdmin
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.



def admin_list(request):
    admins = AdminInfo.objects.all()


    context = {
        "admins": admins
    }
    return render(request, "admins/admin_list.html", context)


def single_admin(request, admin_id):
    single_admin = get_object_or_404(AdminInfo, pk=admin_id)
  
    context = {
        "single_admin": single_admin,
       
    }
    return render(request, "admins/single_admin.html", context)


def create_admin(request):
    if request.method == "POST":
        forms = CreateAdmin(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Admin Registration Successfully!")
        return redirect("home")
    else:
        forms = CreateAdmin()

    context = {
        "forms": forms
    }
    return render(request, "admins/create_admin.html", context)


def edit_admin(request, pk):
    admin_edit = AdminInfo.objects.get(id=pk)
    edit_admin_forms = CreateAdmin(instance=admin_edit)

    if request.method == "POST":
        edit_admin_forms = CreateAdmin(request.POST, request.FILES or None, instance=admin_edit)

        if edit_admin_forms.is_valid():
            edit_admin_forms.save()
            messages.success(request, "Edit admin Info Successfully!")
            return redirect("home")

    context = {
        "edit_admin_forms": edit_admin_forms
    }
    return render(request, "admins/edit_admin.html", context)


def delete_admin(request, admin_id):
    admin_delete = AdminInfo.objects.get(id=admin_id)
    admin_delete.delete()
    messages.success(request, "Delete Admin Info Successfully")
    return redirect("home")










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
            studentProfiles = AdminInfo.objects.create( name = users , admin_email=users.email,full_name=users.get_full_name())
            studentProfiles.save()

            new_user.save()
          
            login(request, new_user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'admins/registration/register.html', context)
