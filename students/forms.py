from django import forms
from .models import StudentInfo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"
        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-control'}),
       
        }



class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="Required")
    
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")
    