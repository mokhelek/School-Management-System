from django.urls import path
from . import views

app_name="admins"
urlpatterns = [
    path('alladmins/', views.admin_list, name='admin_list'),
    path('<int:admin_id>/', views.single_admin, name='single_admin'),
    path('registration/', views.create_admin, name='create_admin'),
    path('edit/<int:pk>', views.edit_admin, name='edit_admin'),
    path('delete/<int:admin_id>', views.delete_admin, name='delete_admin'),
    path('register/', views.register, name='register'),
]
