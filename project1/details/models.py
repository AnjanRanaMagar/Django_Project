from django.db import models

class Model1(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    # Dob = models.DateField()
    Roll_Number = models.IntegerField()
    Department_Name = models.CharField(max_length=225)
    Courses_Name = models.CharField(max_length=225)
    Semester_Number = models.IntegerField()

    # from django.utils import timezone
    # def get_age(self):
    #     today = timezone.now()
    #     return f'You are {(int(Dob[:4])-int(today[:4]))} years old this year.'

class Model2(models.Model):
    # department_relation= models.ForeignKey(Model1,on_delete=models.CASCADE)
    Department_Name = models.CharField(max_length=225)
    No_of_courses = models.IntegerField()
    Number_of_teacher = models.IntegerField()
