from django.contrib import admin
from .models import Student, Department

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'roll_number', 'department', 'created']
    list_filter = ['department', 'created']
    search_fields = ['name', 'roll_number']
    ordering = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dept_name', 'dept_code']