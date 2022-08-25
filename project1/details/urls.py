
from .import views
# from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.index, name='index'),
    path('add/',views.add, name='add'),
    path('add/addrecord/',views.addrecord, name='addrecord'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
    path('index_two',views.index_two, name='index_two'),

    path('add_dp/', views.add_dp, name="add_dp"),
    path('add_dp/addrecord_dp/',views.addrecord_dp,name="addrecord_dp"),
    path('delete_dp/<int:id>',views.delete_dp,name="delete_dp"),
    path('update_dp/<int:id>',views.update_dp,name="update_dp"),
    path('update_dp/updaterecord_dp/<int:id>',views.updaterecord_dp,name="updaterecord_dp"),


]