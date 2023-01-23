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