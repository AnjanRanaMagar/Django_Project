from django.contrib import admin
from .models import Model1, Model2
from .models import Student, Department


admin.site.register(Student),
admin.site.register(Department),
