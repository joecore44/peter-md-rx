from django.shortcuts import render, redirect
from .forms import PatientCreateForm, PatientUpdateForm, ExtendedPatientCreateForm
from .forms import MedicationOrderForm
from .models import PatientProfile, MedicationOrder
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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
    pc_form = ExtendedPatientCreateForm(instance=patient)
    mo_form = MedicationOrderForm(instance=patient)
    
    if request.method == 'POST':
        pc_form = PatientCreateForm(request.POST, instance=patient)
        mo_form = MedicationOrderForm(request.POST, instance=patient)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
        if mo_form.is_valid():
            patient = mo_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'mo_form': mo_form
    }
    return render(request, './content/client-front-form-v1.html', context)

def send_patient_form(request, slug):
    patient = PatientProfile.objects.get(slug=slug)
    if MedicationOrder.objects.filter(patient=patient).exists():
        medication_order = MedicationOrder.objects.get(patient=patient)
        template_context = {
        'first_name': patient.first_name,
        'form_url': '127.0.0.1:8000/forms/'+str(patient.slug)+'/'+str(medication_order.slug)
        }
        template = render_to_string('./content/emails/email-template-1.html', template_context)
        send_mail(
            f'{patient.first_name}: ORDER Medication Now With Peter Uncaged MD',
            template,
            settings.EMAIL_HOST_USER,
            [patient.email],
            fail_silently=False,
            html_message=template,
        )
        return redirect('dashboard')
    else:
        order_form = MedicationOrder.objects.create(patient=patient)

        template_context = {
        'first_name': patient.first_name,
        'form_url': '127.0.0.1:8000/forms/'+str(patient.slug)+'/'+str(order_form.slug)
        }
        template = render_to_string('./content/emails/email-template-1.html', template_context)
        send_mail(
            f'{patient.first_name}: ORDER Medication Now With Peter Uncaged MD',
            template,
            settings.EMAIL_HOST_USER,
            [patient.email],
            fail_silently=False,
            html_message=template,
        )
        return redirect('dashboard')



