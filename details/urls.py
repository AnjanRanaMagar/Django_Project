
from .import views
# from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.index, name='index'),
    path('index_two',views.index_two, name='index_two'),
]