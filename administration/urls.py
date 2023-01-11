from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_home, name='dashboard'), 
    path('/patient/<str:slug>', views.edit_patient, name='edit-patient'),
    path('/patient/<str:slug>/delete', views.delete_patient, name='delete-patient'),
]