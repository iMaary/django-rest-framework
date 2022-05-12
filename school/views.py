from rest_framework import viewsets
from school.models import Student, Course
from school.serializer import StudentSerializer, CourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing Every Students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'head']

class CoursesViewSet(viewsets.ModelViewSet):
    """Showing Every Courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
