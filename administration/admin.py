from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import StaffCreationForm, StaffChangeForm
from .models import Staff, PatientProfile, MedicationOrder

class CustomUserAdmin(UserAdmin):
    add_form = StaffCreationForm
    form = StaffChangeForm
    model = Staff
    list_display = ['email', 'username',]

admin.site.register(Staff, CustomUserAdmin)
admin.site.register(PatientProfile)
admin.site.register(MedicationOrder)