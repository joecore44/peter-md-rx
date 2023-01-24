from django.shortcuts import render, redirect
#from .forms import PatientCreateForm, PatientUpdateForm, ExtendedPatientCreateForm
#from .forms import MedicationOrderForm
from . import forms
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
    pc_form = forms.PatientCreateForm()
    
    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST)
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
    pc_form = forms.PatientCreateForm(instance=patient)
    pu_form = forms.PatientUpdateForm(instance=patient)
    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST, instance=patient)
        pu_form = forms.PatientUpdateForm(request.POST, instance=patient)
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
    pc_form = forms.ExtendedPatientCreateForm(instance=patient)
    mo_form = forms.MedicationOrderForm(instance=patient)
    
    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST, instance=patient)
        mo_form = forms.MedicationOrderForm(request.POST, instance=patient)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
        if mo_form.is_valid():
            patient = mo_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'mo_form': mo_form,
        'testosterone_form': forms.TestosteroneForm,
        'medical_request_form': forms.MedicalRequestForm,
        'additional_medication_form': forms.AdditionalMedicationForm,
        'signature_required_form': forms.SignatureRequiredForm,
        'sharps_container_form': forms.SharpsContainerForm,
        'alcohol_prep_boxes_form': forms.AlcoholPrepBoxesForm,
        'enclomphene_form': forms.EnclomipheneForm,
        'hcg_form': forms.HcgForm,
        'gonadorelin_form': forms.GonadorelinForm,
        'semaglutidel1_form': forms.SemaglutideL1Form,
        'semaglutidel2_form': forms.SemaglutideL2Form,
        'b12_form': forms.B12Form,
        'mic_b12_form': forms.MicB12Form,
        'mic_oral_form': forms.MicOralForm,
        'phentermine_form': forms.PhentermineForm,
        'sildenafil_form': forms.SildenafilForm,
        'tadalafil_form': forms.TadalafilForm,
        'ed_max_form': forms.EdMaxForm,
        'finasteride_form': forms.FinasterideForm,
        'hair_loss_form': forms.HairLossForm,
        'dhea_form': forms.DheaForm,
        'pregnelone_form': forms.PregneloneForm,
        'cabergoline_form': forms.CabergolineForm,
        'glutathione_form': forms.GlutathioneForm,
        'sermorelin_form': forms.SermorelinForm,
        'sermorelinp_form': forms.SermorelinPForm,
        'bpc_form': forms.BpcForm,
        'bpcc_form': forms.BpcCForm,
        'mk677_form': forms.Mk677Form,
        'ipa_cjc_form': forms.IpaCjcForm,
        'ipa_form': forms.IpaForm,
        'modafanil_form': forms.ModafanilForm,
        'metformin_form': forms.MetforminForm,
        'shipping_form': forms.ShippingForm

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



