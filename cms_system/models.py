from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
