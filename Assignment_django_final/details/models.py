from django.db import models
from datetime import date

class Student(models.Model):
    '''Model1 is a name given for the Student Model and has following attribute related to Students'''
    firstname = models.CharField(max_length=225, blank=False, null=False,db_column="FirstName")
    lastname = models.CharField(max_length=225)
    Dob = models.CharField(max_length=100,default='',blank=False, null=True)
    Roll_Number = models.IntegerField()
    Department_Name = models.CharField(max_length=225,blank=False, null=False)
    Courses_Name = models.CharField(max_length=225)
    Semester_Number = models.IntegerField()
    Age = models.BooleanField(default=18)

    def __str__(self):
        return self.firstname

    # def calculate_age(self):
    #     this_year = date.today()
    #     self.Age == int(str(this_year[:4]))-int(Dob[:4])
    #     if self.Age > 6:
    #         self.Age = 8
    #     else:
    #         self.Age= False


class Department(models.Model):
    '''Model2 is a name given for the School Department and has following attributes related to School.'''
    Department_Name = models.CharField(max_length=225,blank=False, null=True)
    No_of_courses = models.IntegerField()
    Number_of_teacher = models.IntegerField()

    def __str__(self):
        return self.Department_Name