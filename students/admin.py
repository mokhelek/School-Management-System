from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(StudentModules)
admin.site.register(Venues)
admin.site.register(StudentSession)
admin.site.register(StudentInfo)
admin.site.register(Attendance)

