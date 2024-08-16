from django.contrib import admin
from .models import StudentTable
# Register your models here.
@admin.register(StudentTable)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','age','city')
