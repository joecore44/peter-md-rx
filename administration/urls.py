from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_home, name='dashboard'), 
    path('/patients', views.staff_patients, name='view-patients'),
    path('/patients/<str:slug>/form/<str:form_slug>', views.staff_view_patient_form, name='view-patient-form'),
    path('/forms', views.staff_forms, name='view-forms'),
    path('/patient/<str:slug>', views.edit_patient, name='edit-patient'),
    path('/patient/<str:slug>/delete', views.delete_patient, name='delete-patient'),
    path('/send-form/<str:slug>', views.send_patient_form, name='send-form'),
    path('/rx-test', views.TestTemplate, name="rx-test"),
    path('/rx-pdf/<str:slug>/<str:form_slug>', views.render_pdf, name="rx-view"),
    
]