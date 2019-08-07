from django.shortcuts import render
from rest_frameowork import viewsets
from .models import Course
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = StudentSerializer
