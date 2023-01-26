from django.shortcuts import render, redirect
#from .forms import PatientCreateForm, PatientUpdateForm, ExtendedPatientCreateForm
#from .forms import MedicationOrderForm
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from . import forms
from .models import PatientProfile, MedicationOrder, PatientActivity
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


def TestTemplate(request):
    return render(request, './content/rx/template-v1.html')

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

def staff_patients(request):
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
    return render(request, './content/staff-patients.html', context)

def staff_forms(request):
    patients = PatientProfile.objects.all()
    pc_form = forms.PatientCreateForm()
    order_forms = MedicationOrder.objects.all()
    
    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patients': patients,
        'pc_form': pc_form,
        'forms': order_forms
    }
    return render(request, './content/staff-forms.html', context)

def edit_patient(request, slug):
    patient = PatientProfile.objects.get(slug=slug)
    pc_form = forms.PatientCreateForm(instance=patient)
    pu_form = forms.PatientUpdateForm(instance=patient)
    activities = PatientActivity.objects.filter(patient=patient).all().order_by('-date_time')[:5]
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
        'pu_form': pu_form,
        'activities': activities
    }
    return render(request, './content/staff-patient-profile.html', context)

def delete_patient(request, slug):
    patient = PatientProfile.objects.get(slug=slug)
    patient.delete()
    return redirect('dashboard')

def patient_fill_form(request, slug, form_slug):
    patient = PatientProfile.objects.get(slug=slug)
    form = MedicationOrder.objects.get(patient=patient, slug=form_slug)
    pc_form = forms.ExtendedPatientCreateForm(instance=patient)
    #mo_form = forms.MedicationOrderForm(instance=patient)
    activity = PatientActivity.objects.create(patient=patient)
    activity.action = 'User'
    activity.value = 'Viewed Form: Medication Order Form'
    activity.save()

    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST, instance=patient)
        #mo_form = forms.MedicationOrderForm(request.POST, instance=patient)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'testosterone_form': forms.TestosteroneForm(instance=form),
        'medical_request_form': forms.MedicalRequestForm(instance=form),
        'additional_medication_form': forms.AdditionalMedicationForm(instance=form),
        'signature_required_form': forms.SignatureRequiredForm(instance=form),
        'sharps_container_form': forms.SharpsContainerForm(instance=form),
        'alcohol_prep_boxes_form': forms.AlcoholPrepBoxesForm(instance=form),
        'enclomphene_form': forms.EnclomipheneForm(instance=form),
        'hcg_form': forms.HcgForm(instance=form),
        'gonadorelin_form': forms.GonadorelinForm(instance=form),
        'semaglutidel1_form': forms.SemaglutideL1Form(instance=form),
        'semaglutidel2_form': forms.SemaglutideL2Form(instance=form),
        'b12_form': forms.B12Form(instance=form),
        'mic_b12_form': forms.MicB12Form(instance=form),
        'mic_oral_form': forms.MicOralForm(instance=form),
        'phentermine_form': forms.PhentermineForm(instance=form),
        'sildenafil_form': forms.SildenafilForm(instance=form),
        'tadalafil_form': forms.TadalafilForm(instance=form),
        'ed_max_form': forms.EdMaxForm(instance=form),
        'finasteride_form': forms.FinasterideForm(instance=form),
        'hair_loss_form': forms.HairLossForm(instance=form),
        'dhea_form': forms.DheaForm(instance=form),
        'pregnelone_form': forms.PregneloneForm(instance=form),
        'cabergoline_form': forms.CabergolineForm(instance=form),
        'glutathione_form': forms.GlutathioneForm(instance=form),
        'sermorelin_form': forms.SermorelinForm(instance=form),
        'sermorelinp_form': forms.SermorelinPForm(instance=form),
        'bpc_form': forms.BpcForm(instance=form),
        'bpcc_form': forms.BpcCForm(instance=form),
        'mk677_form': forms.Mk677Form(instance=form),
        'ipa_cjc_form': forms.IpaCjcForm(instance=form),
        'ipa_form': forms.IpaForm(instance=form),
        'modafanil_form': forms.ModafanilForm(instance=form),
        'metformin_form': forms.MetforminForm(instance=form),
        'shipping_form': forms.ShippingForm(instance=form),
        'slug': form_slug

    }
    return render(request, './content/client-front-form-v1.html', context)

def staff_view_patient_form(request, slug, form_slug):
    patient = PatientProfile.objects.get(slug=slug)
    activities = PatientActivity.objects.filter(patient=patient).all().order_by('-date_time')[:5]
    pc_form = forms.ExtendedPatientCreateForm(instance=patient)
    mo_form = forms.MedicationOrderForm(instance=patient)

    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST, instance=patient)
        mo_form = forms.MedicationOrderForm(request.POST, instance=patient)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
        if mo_form.is_valid():
            order = mo_form.save()
            return redirect('edit-patient', slug=patient.slug)
    
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'mo_form': mo_form,
        'activities': activities
    }
    return render(request, './content/staff-view-form-detail.html', context)

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

def update_patient_form(request, slug, field, val):
    
    if request.method == 'GET':
        medication_order = MedicationOrder.objects.get(slug=slug)
        patient = PatientProfile.objects.get(slug=medication_order.patient.slug)
        if field == 'testosterone':
            medication_order.testosterone = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'medical_requests':
            medication_order.medical_requests = val
            medication_order.save()
            response = {'success': medication_order.medical_requests}
            return JsonResponse(response)
        if field == 'additional_medication':
            medication_order.additional_medication = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'signature_required':
            medication_order.signature_required = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'sharps_container':
            medication_order.sharps_container = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'alcohol_prep_boxes':
            medication_order.alcohol_prep_boxes = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'enclomiphene':
            medication_order.enclomiphene = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'hcg':
            medication_order.hcg = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'gonadorelin':
            medication_order.gonadorelin = val
            medication_order.save()
        if field == 'semaglutide_l1':
            medication_order.semaglutide_l1 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'semaglutide_l2':
            medication_order.semaglutide_l2 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'b12':
            medication_order.b12 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'mic_b12':
            medication_order.mic_b12 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'mic_oral':
            medication_order.mic_oral = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'phentermine':
            medication_order.phentermine = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'sildenafil':
            medication_order.sildenafil = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'tadalafil':
            medication_order.tadalafil = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'ed_max':
            medication_order.ed_max = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'finasteride':
            medication_order.finasteride = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'hair_loss':
            medication_order.hair_loss = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'dhea':
            medication_order.dhea = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'pregnelone':
            medication_order.pregnelone = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'cabergoline':
            medication_order.cabergoline = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'glutathione':
            medication_order.glutathione = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'sermorelin':
            medication_order.sermorelin = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'sermorelinp':
            medication_order.sermorelinp = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'bpc':
            medication_order.bpc = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'bpcc':
            medication_order.bpcc = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'mk677':
            medication_order.mk677 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'ipa_cjc':
            medication_order.ipa_cjc = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'ipa':
            medication_order.ipa = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'modafanil':
            medication_order.modafanil = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'metformin':
            medication_order.metformin = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'shipping':
            medication_order.shipping = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'status':
            if val == 'done':
                patient.status = 'New Submission'
                patient.save()
                activity = PatientActivity.objects.create(patient=patient)
                activity.action = 'Form:'
                activity.value = 'Order Form Submitted'
                activity.save()
                return redirect('dashboard')

provider = {
    'first_name': 'John',
    'last_name': 'Doe',
    'address': '1234 Main St',
    'city': 'Anytown',
    'state': 'CA',
    'zip': '12345',
    'phone': '123-456-7890',
    'fax': '123-456-7890',
    'email': 'telehormonesmd@gmail.com',
    'dea_number': '123456789',
    'practice_name': 'TelehormonesMD',
    'npi_number': '123456789',
}

def render_pdf(request, slug, form_slug):
    patient = PatientProfile.objects.get(slug=slug)
    medication_order = MedicationOrder.objects.get(slug=form_slug)
    context = {
        'provider': provider,
        'patient': patient,
        'medication_order': medication_order,
    }
    pdf = render_to_pdf('./content/rx/template-v1.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
        
'''class ViewPDF(View):
	patient = PatientProfile.objects.get(slug=slug)
    context = {
            'provider': provider,
            'patient': patient,
        }
    def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('./content/rx/template-v1.html')
		return HttpResponse(pdf, content_type='application/pdf')
'''
        


        



