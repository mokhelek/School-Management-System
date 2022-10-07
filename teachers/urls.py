from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path('allteachers/', views.teacher_list, name='teacher_list'),
    path('<int:teacher_id>/', views.single_teacher, name='single_teacher'),
    path('registration/', views.create_teacher, name='create_teacher'),
    path('edit/<int:pk>', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>', views.delete_teacher, name='delete_teacher'),
    
    path('register/', views.register, name='register'),
    path('session/', views.session, name='session'),
    path('single_session/<int:session_id>/', views.single_session, name='single_session'),
]

