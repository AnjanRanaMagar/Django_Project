
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Model1,Model2

def index(request):
    student = Model1.objects.all().values()
    template =loader.get_template('index.html')
    context ={
        'student':student,
    }
    return HttpResponse(template.render(context,request))

    # output =''
    # for x in student:
    #     output+= x['firstname']
    # return HttpResponse(output)
    # template =loader.get_template('myassignment.html')
    # return HttpResponse(template.render())

def index_two(request):
    school = Model2.objects.all().values()
    template =loader.get_template('index_two.html')
    context2 ={
        'school':school,
    }
    return HttpResponse(template.render(context2,request))
