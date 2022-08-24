from django.contrib import admin
from .models import Model1 as Student
from .models import Model2 as Department

# Register your models here. username = ANJAN, PSW: myWallet5$
admin.site.register(Student),
admin.site.register(Department),