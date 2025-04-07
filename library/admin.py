from django.contrib import admin
from .models import Course, Student

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1  # Number of blank forms displayed

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')
    search_fields = ('name',)
    inlines = [StudentInline]  # Enables inline editing

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'course')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('course',)
