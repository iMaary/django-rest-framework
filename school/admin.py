from re import search
from django.contrib import admin
from school.models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_link = ('id', 'name')
    search_field = ('name')
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code_course', 'description')
    list_display_link = ('id', 'code_course')
    search_field = ('code_course')

admin.site.register(Course, Courses)
