from django.db import models
from django.utils import timezone
from datetime import date


class Student(models.Model):
    '''Model1 is a name given for the Student Model and has following attribute related to Students'''
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    Dob= models.DateField(verbose_name="Y-M-D")
    Roll_Number = models.IntegerField()
    Department_Name = models.CharField(max_length=225)
    Courses_Name = models.CharField(max_length=225)
    Semester_Number = models.IntegerField()
    Age = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname


class Department(models.Model):
    '''Model2 is a name given for the School Department and has following attributes related to School.'''
    Department_Name = models.CharField(max_length=225)
    No_of_courses = models.IntegerField()
    Number_of_teacher = models.IntegerField()

    def __str__(self):
        return self.Department_Name