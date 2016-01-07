from __future__ import unicode_literals

from django.db import models

# Create your models here.
import collections
from django.forms import ModelForm

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    office_details = models.CharField(max_length=30)
    phone= models.IntegerField()
    email = models.EmailField()
class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=15)
    course_classroom = models.CharField(max_length=20)
    course_times = models.DateField()
    course_student = models.ManyToManyField(Student)
    course_teacher = models.OneToOneField(Teacher)

