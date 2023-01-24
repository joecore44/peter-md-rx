from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff, PatientProfile, MedicationOrder

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

class ExtendedPatientCreateForm(forms.ModelForm):
    
    class Meta:
        model = PatientProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'city',
            'state',
            'zip_code',

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
class MedicationOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicationOrderForm, self).__init__(*args, **kwargs)
        self.fields['testosterone'].label = '''
            TESTOSTERONE (COVERED IN MONTHLY COST up to 200mg weekly). Select N/A if you are not due for testosterone and are only adding extra medications.<br />
            Please select needle size for injecting testosterone - Default IM (intramuscular: into the muscle)- 25g Injecting needle with 20g drawing needle. Default SUBQ(Subcutaneous: into the fatty tissue)- 30g x 1/2" x 1ml Insulin needle (no drawing needle available for insulin needles). Insulin needles can also be used for shallow intramuscular injecting. The main difference is the size of the needle. If you prefer a specific size please add your requests in the comment section below.(Required)<br /><br />

            IF you are on the ENCLOMIPHENE program (sep f/ testosterone program) select enclomiphene. NO SUPPLIES NECESSARY. Select N/A if you are not due for enclomiphene and are only adding extra medications. *
        '''

    class Meta:
        model = MedicationOrder
        fields = [
            'testosterone',
            'medical_requests',
            'additional_medication',
            'signature_required',
            'sharps_container',
            'alcohol_prep_boxes',
        ]

class TestosteroneForm(forms.ModelForm):
    
    class Meta:
        model = MedicationOrder
        fields = [
            'testosterone',
        ]
class MedicalRequestForm(forms.ModelForm):
    
    class Meta:
        model = MedicationOrder
        fields = [
            'medical_requests',
        ]
class AdditionalMedicationForm(forms.ModelForm):
    
    class Meta:
        model = MedicationOrder
        fields = [
            'additional_medication',
        ]
class SignatureRequiredForm(forms.ModelForm):
    
    class Meta:
        model = MedicationOrder
        fields = [
            'signature_required',
        ]
class SharpsContainerForm(forms.ModelForm):
        
        class Meta:
            model = MedicationOrder
            fields = [
                'sharps_container',
            ]
class AlcoholPrepBoxesForm(forms.ModelForm):
        
        class Meta:
            model = MedicationOrder
            fields = [
                'alcohol_prep_boxes',
            ]
class EnclomipheneForm(forms.ModelForm):
        
        class Meta:
            model = MedicationOrder
            fields = [
                'enclomiphene',
            ]
class HcgForm(forms.ModelForm):
        
        class Meta:
            model = MedicationOrder
            fields = [
                'hcg_5000',
            ]
class GonadorelinForm(forms.ModelForm):
        
        class Meta:
            model = MedicationOrder
            fields = [
                'gonadorelin',
            ]
class SemaglutideL1Form(forms.ModelForm):
        
        class Meta:
            model = MedicationOrder
            fields = [
                'semaglutide_l1',
            ]
class SemaglutideL2Form(forms.ModelForm):
            
            class Meta:
                model = MedicationOrder
                fields = [
                    'semaglutide_l2',
                ]
class B12Form(forms.ModelForm):
            
            class Meta:
                model = MedicationOrder
                fields = [
                    'b12_10ml',
                ]
class MicB12Form(forms.ModelForm):
            
            class Meta:
                model = MedicationOrder
                fields = [
                    'mic_b12',
                ]
class MicOralForm(forms.ModelForm):
            
            class Meta:
                model = MedicationOrder
                fields = [
                    'mic_oral',
                ]
class PhentermineForm(forms.ModelForm):
            
            class Meta:
                model = MedicationOrder
                fields = [
                    'phentermine',
                ]
class SildenafilForm(forms.ModelForm):
            
            class Meta:
                model = MedicationOrder
                fields = [
                    'sildenafil',
                ]
class TadalafilForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'tadalafil',
                ]
class EdMaxForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'ed_max',
                ]
class FinasterideForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'finasteride',
                ]
class HairLossForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'hair_loss',
                ]
class DheaForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'dhea',
                ]
class PregneloneForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'pregnelone',
                ]
class CabergolineForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'cabergoline',
                ]
class GlutathioneForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'glutathione',
                ]
class SermorelinForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'sermorelin',
                ]
class SermorelinPForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'sermorelin_p',
                ]
class BpcForm(forms.ModelForm):
                
            class Meta:
                model = MedicationOrder
                fields = [
                    'bpc_157',
                ]
class BpcCForm(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'bpc_157_c',
                ]
class Mk677Form(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'mk_677',
                ]
class IpaCjcForm(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'ipa_cjc',
                ]
class IpaForm(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'ipa',
                ]
class ModafanilForm(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'modafanil',
                ]
class MetforminForm(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'metformin',
                ]
class ShippingForm(forms.ModelForm):
                    
            class Meta:
                model = MedicationOrder
                fields = [
                    'expedited_shipping',
                ]