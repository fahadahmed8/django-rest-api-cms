from rest_framework import serializers
from .models import Student, Course, Degree

class DegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degree
        fields = ('id', 'url', 'name')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'url', 'name', 'roll_no', 'degree', 'course')
