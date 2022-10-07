from django import forms
from .models import AdminInfo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateAdmin(forms.ModelForm):
    class Meta:
        model = AdminInfo
        fields = "__all__"

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="Required")
    
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")
    