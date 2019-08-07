from django.db import models


class Degree(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


    

