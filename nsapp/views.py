from rest_framework import generics
from .models import Course,Instructor
from .serializers import CourseSerializer,InstructorSerializer

class InstructorListView(generics.ListCreateAPIView):
    serializer_class=InstructorSerializer
    queryset=Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    serializer_class=CourseSerializer
    queryset=Course.objects.all()

