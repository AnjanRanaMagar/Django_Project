from django.db import models

class Model1(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    # Dob =
    Roll_Number = models.IntegerField()
    Department_Name = models.CharField(max_length=225)
    Courses_Name = models.CharField(max_length=225)
    Semester_Number = models.IntegerField()

class Model2(models.Model):
    Department_Name = models.CharField(max_length=225)
    No_of_courses = models.IntegerField()
    Number_of_teacher = models.IntegerField()
