from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from . import forms
from .models import PatientProfile, MedicationOrder, PatientActivity
from .models import OrderItem, PatientOrder, Provider
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def log_in(request):
    return render(request, './content/login.html')

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

@login_required
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

@login_required
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

@login_required
def staff_forms(request):
    patients = PatientProfile.objects.all()
    pc_form = forms.PatientCreateForm()
    order_forms = MedicationOrder.objects.all()
    orders = PatientOrder.objects.all()
    
    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('edit-patient', slug=patient.slug)
    context = {
        'patients': patients,
        'pc_form': pc_form,
        'forms': order_forms,
        'orders': orders
    }
    return render(request, './content/staff-forms.html', context)

@login_required
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

@login_required
def delete_patient(request, slug):
    patient = PatientProfile.objects.get(slug=slug)
    patient.delete()
    return redirect('dashboard')

@login_required
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
        'gonadorelin_n_form': forms.GonadorelinNForm(instance=form),
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
        'syringes_form': forms.SyringesForm(instance=form),
        'slug': form_slug

    }
    return render(request, './content/client-front-form-v1.html', context)
@login_required
def staff_view_patient_form(request, slug, form_slug, order_slug):
    patient = PatientProfile.objects.get(slug=slug)
    order = PatientOrder.objects.get(slug=order_slug)
    form = MedicationOrder.objects.get(patient=patient, slug=form_slug)
    activities = PatientActivity.objects.filter(patient=patient).all().order_by('-date_time')[:5]
    pc_form = forms.ExtendedPatientCreateForm(instance=patient)
    mo_form = forms.MedicationOrderForm(instance=form)
    st_form = forms.OrderStatusForm(instance=order)

    if request.method == 'POST':
        pc_form = forms.PatientCreateForm(request.POST, instance=patient)
        mo_form = forms.MedicationOrderForm(request.POST, instance=form)
        st_form = forms.OrderStatusForm(request.POST, instance=order)
        if pc_form.is_valid():
            patient = pc_form.save()
            return redirect('view-patient-form', slug=patient.slug, form_slug=form_slug, order_slug=order_slug)
        if mo_form.is_valid():
            order = mo_form.save()
            return redirect('view-patient-form', slug=patient.slug, form_slug=form_slug, order_slug=order_slug)
        if st_form.is_valid():
            order = st_form.save()
            return redirect('view-patient-form', slug=patient.slug, form_slug=form_slug, order_slug=order_slug)
    
    context = {
        'patient': patient,
        'pc_form': pc_form,
        'mo_form': mo_form,
        'activities': activities,
        'st_form': st_form,
        'order': order
    }
    return render(request, './content/staff-view-form-detail.html', context)

@login_required
def staff_medication_order(request, slug):
    order = PatientOrder.objects.get(slug=slug)
    patient = PatientProfile.objects.get(slug=order.patient.slug)
    order_items = OrderItem.objects.filter(order=order).all()
    form = MedicationOrder.objects.filter(patient=patient).first()
    context = {
        'patient': patient,
        'order': order,
        'order_items': order_items,
        'form': form
    }
    return render(request, './content/staff-medication-order.html', context)


@login_required
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

@login_required
def staff_delete_order(request, slug):
    order = PatientOrder.objects.get(slug=slug)
    order.delete()
    return redirect('view-forms')

@login_required
def update_patient_form(request, slug, field, val):
    
    if request.method == 'GET':
        medication_order = MedicationOrder.objects.get(slug=slug)
        patient = PatientProfile.objects.get(slug=medication_order.patient.slug)
        if field == 'first_name':
            patient.first_name = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'last_name':
            patient.last_name = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'email':
            patient.email = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'phone':
            patient.phone = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'address':
            patient.address = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'city':
            patient.city = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'state':
            patient.state = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'zip_code':
            patient.zip_code = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'additional_information':
            patient.additional_information = val
            patient.save()
            response = {'success': True}
            return JsonResponse(response)
        
        
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
        if field == 'hcg_5000':
            medication_order.hcg_5000 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'gonadorelin':
            medication_order.gonadorelin = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'gonadorelin_nasal':
            medication_order.gonadorelin_nasal = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
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
        if field == 'b12_10ml':
            medication_order.b12_10ml = val
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
        if field == 'sermorelin_p':
            medication_order.sermorelin_p = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'bpc_157':
            medication_order.bpc_157 = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'bpc_157_c':
            medication_order.bpc_157_c = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'mk_677':
            medication_order.mk_677 = val
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
        if field == 'syringes':
            medication_order.syringes = val
            medication_order.save()
            response = {'success': True}
            return JsonResponse(response)
        if field == 'expedited_shipping':
            medication_order.expedited_shipping = val
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
                order = PatientOrder.objects.create(patient=patient)
                for field in medication_order._meta.get_fields():
                    if field.name != 'id' and field.name != 'patient' and field.name != 'slug' and field.name != 'medical_requests':
                        if getattr(medication_order, field.name) != 'NA' and getattr(medication_order, field.name) != 'No' and getattr(medication_order, field.name) != '0':
                            item = OrderItem.objects.create(order=order, quantity=0)
                            name2 = ' '
                            name3 = ' '
                            size = ' '
                            instructions = ' '
                            if field.name == 'testosterone':
                                if getattr(medication_order, field.name) != 'ENCLOMIPHENE':
                                    name = 'Testosterone Cypionate 200mg'
                                    size = '10ml'
                                    quantity = 1
                                    instructions = ' '
                                    name2 = '25G X 1"'
                                    size2 = ' '
                                    quantity2 = '30'
                                    instructions2 = 'Use to inject Testosterone'
                                    name3 = '20G X 1.5" 3ML'
                                    size3 = ' '
                                    quantity3 = '30'
                                    instructions3 = 'Use to draw test from vial'
                                else:
                                    name = 'Enclomiphene 12.5mg'
                                    size = '12.5mg'
                                    quantity = 30
                                    instructions = 'Take one tab by mouth daily'
                            if field.name == 'sharps_container':
                                name = 'Sharps Container'
                                size = '3 containers'
                                if getattr(medication_order, field.name) == 'Yes':
                                    quantity = 3
                                else:
                                    quantity = 0
                                instructions = ' '
                            if field.name == 'enclomiphene':
                                name = 'Enclomiphene 12.5mg'
                                size = '12.5mg'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take one tab by mouth daily'
                            if field.name == 'alcohol_prep_boxes':
                                name = 'Alcohol Prep Boxes'
                                size = 'box(s)'
                                quantity = getattr(medication_order, field.name)
                                instructions = ' '
                            if field.name == 'hcg_5000':
                                name = 'HCG 5000iu'
                                name2 = 'Mixing Syringe and BAC Water'
                                size2 = ' '
                                quantity2 = '1'
                                instructions2 = 'Add 5ml BAC to HCG'
                                name3 = '30G X 5/16" 1ML'
                                size3 = ' '
                                quantity3 = '20'
                                instructions3 = 'use to inject HCG'
                                size = '1 vial'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 25u SUBQ weekly'
                            if field.name == 'gonadorelin':
                                name = 'Gonadorelin'
                                size = '1 vial'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 25u SUBQ weekly'
                                name2 = '30G X 5/16" 1ML'
                                size2 = ' '
                                quantity2 = '20'
                                instructions2 = 'Use to inject gonadorelin'
                            if field.name == 'gonadorelin_nasal':
                                name = 'Gonadorelin Nasal Spray 20MCG/0.1ML'
                                size = '4ml'
                                if getattr(medication_order, field.name) == 'Yes':
                                    quantity = 1
                                else:
                                    quantity = 0
                                instructions = ' '
                            if field.name == 'semaglutide_l1':
                                if getattr(medication_order, field.name) == 'Yes':
                                    name = 'Weeks 1-4 Semaglutide 2MG/ML'
                                    size = '3ml'
                                    quantity = 1
                                    instructions = 'Inject 10U SUBQ weekly'
                                    name2 = 'Weeks 5-8 Semaglutide 2MG/ML'
                                    size2 = ' '
                                    quantity2 = '1'
                                    instructions2 = 'Inject 20U SUBQ weekly'
                                    name3 = '30G X 5/16" 1ML'
                                    size3 = ' '
                                    quantity3 = '20'
                                    instructions3 = 'Use to inject Semaglutide'
                                else:
                                    quantity = 0
                                    instructions = ' '
                            if field.name == 'semaglutide_l2':
                                if getattr(medication_order, field.name) == 'Yes':
                                    name = 'Weeks 9-12 Semaglutide 2MG/ML'
                                    size = '3ml'
                                    quantity = 1
                                    instructions = 'Inject 40U SUBQ weekly'
                                    name2 = 'Weeks 13-16 Semaglutide 2MG/ML'
                                    size2 = ' '
                                    quantity2 = '1'
                                    instructions2 = 'Inject 68U SUBQ weekly'
                                    name3 = '30G X 5/16" 1ML'
                                    size3 = ' '
                                    quantity3 = '40'
                                    instructions3 = 'Use to inject Semaglutide'
                                else:
                                    quantity = 0
                                    instructions = ' '
                            if field.name == 'b12_10ml':
                                name = 'B12'
                                size = '10ML'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 1ML IM weekly'
                                name2 = '25G X 1" 3ML'
                                size2 = ' '
                                quantity2 = '10'
                                instructions2 = 'Use to inject B12'
                            if field.name == 'mic_b12':
                                name = 'B12 + MIC'
                                size = '10ML'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 1ML IM weekly'
                                name2 = '25G X 1" 3ML'
                                size2 = ' '
                                quantity2 = '10'
                                instructions2 = 'use to inject B12 + MIC'
                            if field.name == 'mic_oral':
                                name = 'Methionine / Inositol / Cyanocobalamin / L-Carnitine 25/25/1/100MG'
                                size = ' '
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 tablet by mouth daily'
                            if field.name == 'phentermine':
                                name = 'Phentermine'
                                size = '37.5MG'
                                if getattr(medication_order, field.name) == 'Yes':
                                    quantity = 30
                                    instructions = 'Take 1 tablet by mouth daily'
                                else:
                                    quantity = 0
                                    instructions = ' '
                            if field.name == 'sildenafil':
                                name = 'Sildenafil'
                                size = '100MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1/4 tablet 30mins before sex'
                            if field.name == 'tadalafil':
                                name = 'Tadalafil'
                                size = '20MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1/4 tablet 30mins before sex'
                            if field.name == 'ed_max':
                                name = 'Tadalafil 20MG/Oxytocin 100IU/PT-141 2000MCG'
                                size = '1 bottle'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 tablet by mouth 30 mins before sex'
                            if field.name == 'finasteride':
                                name = 'Finasteride'
                                size = '1MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 tablet by mouth daily'
                            if field.name == 'hair_loss':
                                name = 'Minoxidil/Finasteride/Ketoconazole'
                                size = '50ML'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Spray 10 pumps onto scalp twice daily'
                            if field.name == 'dhea':
                                name = 'DHEA'
                                size = '25MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 tablet by mouth daily'
                            if field.name == 'pregnelone':
                                name = 'Pregnelone 50mg/DHEA50mg tablet'
                                size = ' '
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 tablet by mouth daily'
                            if field.name == 'cabergoline':
                                name = 'Cabergoline'
                                size = '0.5MG'
                                if getattr(medication_order, field.name) == 'Yes':
                                    quantity = 1
                                else:
                                    quantity = 0
                                instructions = 'Take 1 tablet by mouth weekly '
                            if field.name == 'glutathione':
                                name = 'Glutathione 200mg'
                                size = '30ML'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 1ml IM weekly'
                                name2 = '25G X 1" 3ML'
                                size2 = ' '
                                quantity2 = '30'
                                instructions2 = 'use to inject glutathione'
                            if field.name == 'sermorelin':
                                name = 'Sermorelin'
                                size = '9MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = ' '
                                name2 = 'Mixing Syringe & BAC Water'
                                size2 = ' '
                                quantity2 = quantity
                                instructions2 = 'Add 10ML BAC to peptide'
                                name3 = '30G X 5/16" X 1ML'
                                size3 = ' '
                                quantity3 = int(quantity) * 30
                                instructions3 = 'Use to inject peptide'
                            if field.name == 'sermorelin_p':
                                name = 'Sermorelin Troche'
                                size = '300MCG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 tablet by mouth daily'
                            if field.name == 'bpc_157':
                                name = 'BPC157 injectable'
                                size = '10MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 35u SUBQ per day'
                                name2 = 'Mixing Syringe & BAC Water'
                                size2 = ' '
                                quantity2 = quantity
                                instructions2 = 'Add 10ML BAC to peptide'
                                name3 = '30G X 5/16" X 1ML'
                                size3 = ' '
                                quantity3 = int(quantity) * 30
                                instructions3 = 'Use to inject peptide'
                            if field.name == 'bpc_157_c':
                                name = 'BPC157 Capsule 500mcg'
                                size = '500MCG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 capsule by mouth daily'
                            if field.name == 'mk_677':
                                name = 'MK677'
                                size = '25MG'
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Take 1 capsule by mouth daily'
                            if field.name == 'ipa':
                                name = 'Ipamorelin 9mg'
                                size = ' '
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 20U SUBQ daily'
                                name2 = 'Mixing Syringe & BAC Water'
                                size2 = ' '
                                quantity2 = quantity
                                instructions2 = 'Add 6ML BAC to peptide'
                                name3 = '30G X 5/16" X 1ML'
                                size3 = ' '
                                quantity3 = int(quantity) * 30
                                instructions3 = 'Use to inject peptide'
                            if field.name == 'ipa_cjc':
                                name = 'Ipamorelin 9mg/CJC1295 5mg'
                                size = ' '
                                quantity = getattr(medication_order, field.name)
                                instructions = 'Inject 20U SUBQ daily'
                                name2 = 'Mixing Syringe & BAC Water'
                                size2 = ' '
                                quantity2 = quantity
                                instructions2 = 'Add 6ML BAC to peptide'
                                name3 = '30G X 5/16" X 1ML'
                                size3 = ' '
                                quantity3 = int(quantity) * 30
                                instructions3 = 'Use to inject peptide'
                            if field.name == 'modafanil':
                                name = 'Modafanil'
                                size = '200MG'
                                if getattr(medication_order, field.name) == 'Yes':
                                    quantity = 30
                                    instructions = 'Take 1 tablet by mouth daily'
                                else:
                                    quantity = 0
                                    instructions = ' '
                            if field.name == 'metformin':
                                name = 'Metformin'
                                size = '500MG'
                                if getattr(medication_order, field.name) == 'Yes':
                                    quantity = 30
                                    instructions = 'Take 1 by mouth daily'
                                else:
                                    quantity = 0
                                    instructions = ' '


                            item.item = name                           
                            item.size = size
                            item.quantity = quantity
                            item.instructions = instructions
                            item.save()
                            if name2 != ' ':
                                second = OrderItem.objects.create(order=order, quantity=0)
                                second.item = name2
                                second.size = size2
                                second.quantity = quantity2
                                second.instructions = instructions2
                                second.save()
                            if name3 != ' ':
                                third = OrderItem.objects.create(order=order, quantity=0)
                                third.item = name3
                                third.size = size3
                                third.quantity = quantity3
                                third.instructions = instructions3
                                third.save()
                        else:
                            pass
                if not OrderItem.objects.filter(order=order).exists():
                    inst = PatientOrder.objects.get(slug=order.slug)
                    inst.delete()
                        
                        
                response = {'success': True}
                return JsonResponse(response)

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

@login_required
def staff_medication_orders(request):
    medication_orders = PatientOrder.objects.all()
    context = {
        'orders': medication_orders,
    }
    return render(request, './content/staff-orders.html', context)

@login_required
def render_pdf(request, slug, order_slug):
    patient = PatientProfile.objects.get(slug=slug)
    medication_order = PatientOrder.objects.get(slug=order_slug)
    order_items = OrderItem.objects.filter(order=medication_order)
    context = {
        'provider': provider,
        'patient': patient,
        'order_items': order_items,
    }
    pdf = render_to_pdf('./content/rx/template-v1.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
        
        


        



