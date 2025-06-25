from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from rest_framework import generics

#Django Rest

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Create your views here.



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

def home(request):
    return render(request, 'index.html', {})