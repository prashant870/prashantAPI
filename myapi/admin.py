from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Student)
class ModelAdminStudent(admin.ModelAdmin):
    list_display=('id','name','roll','city')