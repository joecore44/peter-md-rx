from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff, PatientProfile

class StaffCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Staff
        fields = ('username', 'email')

class StaffChangeForm(UserChangeForm):
    
        class Meta:
            model = Staff
            fields = ('username', 'email')

class PatientCreateForm(forms.ModelForm):
    
    class Meta:
        model = PatientProfile
        fields = [
            'status',
            'first_name',
            'last_name',
            'email',
            'phone',
        ]
class PatientUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PatientProfile
        fields = [
            'date_of_birth',
            'gender',
            'marital_status',
            'address',
            'city',
            'state',
            'zip_code',
            'emergency_contact_name',
            'emergency_contact_phone',
            'emergency_contact_relationship',
            'additional_information',
        ]