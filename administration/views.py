from django.shortcuts import render, redirect
from .forms import PatientCreateForm, PatientUpdateForm
from .models import PatientProfile

patients_data = [
    {'first_name': 'Jordann',
    'last_name': 'Shepard',
    'email': 'jordann@shepard.com',
    'phone': '555-555-5555'
    }
]

def staff_home(request):
    patients = PatientProfile.objects.all()
    pc_form = PatientCreateForm()
    if request.method == 'POST':
        pc_form = PatientCreateForm(request.POST)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patients': patients,
        'pc_form': pc_form
    }
    return render(request, './content/staff-index2.html', context)

def edit_patient(request, slug):
    patient = PatientProfile.objects.get(slug=slug)
    pc_form = PatientCreateForm(instance=patient)
    pu_form = PatientUpdateForm(instance=patient)
    if request.method == 'POST':
        pc_form = PatientCreateForm(request.POST, instance=patient)
        pu_form = PatientUpdateForm(request.POST, instance=patient)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
        if pu_form.is_valid():
            patient = pu_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'pu_form': pu_form
    }
    return render(request, './content/staff-patient-profile.html', context)

def delete_patient(request, slug):
    patient = PatientProfile.objects.get(slug=slug)
    patient.delete()
    return redirect('dashboard')

def patient_fill_form(request, slug, form_slug):
    patient = PatientProfile.objects.get(slug=slug)
    pc_form = PatientCreateForm(instance=patient)
    pu_form = PatientUpdateForm(instance=patient)
    if request.method == 'POST':
        pc_form = PatientCreateForm(request.POST, instance=patient)
        pu_form = PatientUpdateForm(request.POST, instance=patient)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
        if pu_form.is_valid():
            patient = pu_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'pu_form': pu_form
    }
    return render(request, './content/client-front-form-v1.html', context)