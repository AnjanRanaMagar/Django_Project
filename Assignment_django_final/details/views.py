
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student,Department

def index(request):
    # student = Model1.objects.all().values()
    student = Student.objects.all().values()
    template = loader.get_template('index.html')
    context ={
        'student':student,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def add_dp(request):
    template = loader.get_template('add_dp.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    date = request.POST['dob']
    roll_num=request.POST['roll']
    department=request.POST['dp']
    courses =request.POST['course']
    semester_num=request.POST['semester_num']
    # student = Model1(firstname=x,lastname=y,Dob=date,  Roll_Number=roll_num,Department_Name=department,
    #                  Courses_Name=courses,Semester_Number=semester_num)
    student = Student(firstname=x, lastname=y, Dob=date, Roll_Number=roll_num, Department_Name=department,
                     Courses_Name=courses, Semester_Number=semester_num)
    student.save()
    return HttpResponseRedirect(reverse('index'))


def addrecord_dp(request):
    name_dp = request.POST['dp_name']
    num_dp_course=request.POST['dp_course_num']
    num_dp_teacher=request.POST['dp_teacher_num']
    # department=Model2(Department_Name=name_dp,No_of_courses=num_dp_course,Number_of_teacher=num_dp_teacher)
    department = Department(Department_Name=name_dp, No_of_courses=num_dp_course, Number_of_teacher=num_dp_teacher)
    department.save()
    return HttpResponseRedirect(reverse('index_two'))

def delete(request,id):
    # student =Model1.objects.get(id=id)
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_dp(request,id):
    # department =Model2.objects.get(id=id)
    department = Department.objects.get(id=id)
    department.delete()
    return HttpResponseRedirect(reverse('index_two'))

def update(request,id):
    # student=Model1.objects.get(id=id)
    student = Student.objects.get(id=id)
    template=loader.get_template('update.html')
    context= {
        'student':student,
    }
    return HttpResponse(template.render(context,request))

def update_dp(request,id):
    # department=Model2.objects.get(id=id)
    department = Department.objects.get(id=id)
    template=loader.get_template('update_dp.html')
    context= {
        'department':department,
    }
    return HttpResponse(template.render(context,request))


def updaterecord(request,id):
    # student=Model1.objects.get(id=id)
    student = Student.objects.get(id=id)
    x = request.POST['first']
    student.firstname=x
    y = request.POST['last']
    student.lastname = y
    db =request.POST['dob']
    student.Dob=db
    roll_num = request.POST['roll']
    student.Roll_Number = roll_num
    department = request.POST['dp']
    student.Department_Name = department
    courses = request.POST['course']
    student.Courses_Name = courses
    semester_num = request.POST['semester_num']
    student.Semester_Number = semester_num
    student.save()
    return HttpResponseRedirect(reverse('index'))

def updaterecord_dp(request,id):
    # department=Model2.objects.get(id=id)
    department = Department.objects.get(id=id)
    x = request.POST['dp_name']
    department.Department_Name=x
    y = request.POST['course_num']
    department.No_of_courses = y
    z = request.POST['teacher_num']
    department.Number_of_teacher=z
    department.save()
    return HttpResponseRedirect(reverse('index_two'))

def index_two(request):
    # school = Model2.objects.all().values()
    school = Department.objects.all().values()
    template = loader.get_template('index_two.html')
    context2 ={
        'school':school,
    }
    return HttpResponse(template.render(context2,request))

# def age_calculate(request,Dob):
#     year_born = Model1.objects.get(Dob=Dob)
#     this_year = timezone.now()
#     age = int(year_born[:4])-int(str(this_year[:4]))
#     template = loader.get_template('index.html')
#     context={
#         'age':age,
#     }
#     return HttpResponse(template.render(context, request)



