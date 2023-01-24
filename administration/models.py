from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Staff(AbstractUser):
    
    def __str__(self):
        return self.email

class PatientProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    MARITAL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Domestic Partner', 'Domestic Partner'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Pending', 'Pending'),
        ('Active', 'Active'),
    )
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255, default='(555) 555-5555')
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact_relationship = models.CharField(max_length=255, null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)

class MedicationOrder(models.Model):
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    TEST_CHOICES = (
            ('IM', 'IM (intramuscular) - injecting into the muscle'),
            ('SUBQ', 'SUBQ (Subcutaneous) - injecting into the fatty tissue'),
            ('N/A', 'Not due for testosterone to be filled'),
            ('ENCLOMIPHENE', 'Enclomophine - Clomid'),
        )
    NUMBER_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    CLOMID_CHOICES = (
        ('0', '0'),
        ('30 tabs', '30 tabs $75'),
        ('60 tabs', '60 tabs $145'),
    )
    MIC_CHOICES = (
        ('One Month','One Month: 30 tablets $86.50'),
        ('Two Months','Two Months: 60 tablets $163.50'),
        ('Three Months','Three Months: 90 tablets $241.50'),
    )
    SILDENAFIL_CHOICES = (
        ('10 Tablets','10 Tablets: $62.50'),
        ('15 Tablets','15 Tablets: $90'),
        ('20 Tablets','20 Tablets: $120'),
        ('30 Tablets','30 Tablets: $180'),
    )
    TADALAFIL_CHOICES = (
        ('10 Tablets','10 Tablets: $72.50'),
        ('15 Tablets','15 Tablets: $100'),
        ('20 Tablets','20 Tablets: $140'),
        ('30 Tablets','30 Tablets: $210'),
    )
    ED_MAX_CHOICES = (
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
    )
    FINA_CHOICES = (
        ('30 Tablets','30 Tablets: $40'),
        ('60 Tablets','60 Tablets: $74'),
    )
    DHEA_CHOICES = (
        ('10 Tablets','10 Tablets: $40'),
        ('15 Tablets','15 Tablets: $60'),
        ('20 Tablets','20 Tablets: $75'),
        ('30 Tablets','30 Tablets: $113'),
    )
    PREGNELONE_CHOICES = (
        ('30 Tablets','30 Tablets: $79'),
        ('60 Tablets','60 Tablets: $149'),
    )
    SERMORELIN_CHOICES = (
        ('1 Month', '1 Month $211.65'),
        ('2 Month', '2 Month $400'),
        ('3 Month', '3 Month $598'),
    )
    SERMORELINP_CHOICES = (
        ('1 Month', '1 Month $183'),
        ('2 Month', '2 Month $355'),
        ('3 Month', '3 Month $530'),
    )
    BPC_CHOICES = (
        ('1 Month', '1 Month $226'),
        ('2 Month', '2 Month $400'),
        ('3 Month', '3 Month $600'),
    )
    BPCC_CHOICES = (
        ('1 Month', '1 Month $180'),
        ('2 Month', '2 Month $348'),
        ('3 Month', '3 Month $511'),
    )
    MK677_CHOICES = (
        ('1 Month', '1 Month $195'),
        ('2 Month', '2 Month $380'),
        ('3 Month', '3 Month $570'),
    )
    IPA_CJC_CHOICES = (
        ('1 Month', '1 Month $255'),
        ('2 Month', '2 Month $430'),
        ('3 Month', '3 Month $635'),
    )


    testosterone = models.CharField(max_length=255, choices=TEST_CHOICES, default='N/A')
    medical_requests = models.TextField(verbose_name='Comments or Requests')
    additional_medication = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    signature_required = models.CharField(max_length=25, choices=YES_NO_CHOICES, default='No')
    sharps_container = models.CharField(max_length=25, choices=YES_NO_CHOICES, default='No')
    alcohol_prep_boxes = models.CharField(max_length=3, choices=NUMBER_CHOICES, default='0')
    enclomiphene = models.CharField(max_length=255, choices=CLOMID_CHOICES, default='0')
    hcg_5000 = models.CharField(max_length=25, choices=NUMBER_CHOICES, default='0')
    gonadorelin = models.CharField(max_length=25, choices=NUMBER_CHOICES, default='0')
    semaglutide_l1 = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    semaglutide_l2 = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    b12_10ml = models.CharField(max_length=25, choices=NUMBER_CHOICES, default='0')
    mic_b12 = models.CharField(max_length=25, choices=NUMBER_CHOICES, default='0')
    mic_oral = models.CharField(max_length=25, choices=MIC_CHOICES, default='0')
    phentermine = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    sildenafil = models.CharField(max_length=25, choices=SILDENAFIL_CHOICES, default='0')
    tadalafil = models.CharField(max_length=25, choices=TADALAFIL_CHOICES, default='0')
    ed_max = models.CharField(max_length=25, choices=ED_MAX_CHOICES, default='0')
    finasteride = models.CharField(max_length=25, choices=FINA_CHOICES, default='0')
    hair_loss = models.CharField(max_length=25, choices=NUMBER_CHOICES, default='0')
    dhea = models.CharField(max_length=25, choices=DHEA_CHOICES, default='0')
    pregnelone = models.CharField(max_length=25, choices=PREGNELONE_CHOICES, default='0')
    cabergoline = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    glutathione = models.CharField(max_length=25, choices=NUMBER_CHOICES, default='0')
    sermorelin = models.CharField(max_length=25, choices=SERMORELIN_CHOICES, default='0')
    sermorelin_p = models.CharField(max_length=25, choices=SERMORELINP_CHOICES, default='0')
    bpc_157 = models.CharField(max_length=25, choices=BPC_CHOICES, default='0')
    bpc_157_c = models.CharField(max_length=25, choices=BPCC_CHOICES, default='0')
    mk_677 = models.CharField(max_length=25, choices=MK677_CHOICES, default='0')
    ipa_cjc = models.CharField(max_length=25, choices=IPA_CJC_CHOICES, default='0')
    ipa = models.CharField(max_length=25, choices=IPA_CJC_CHOICES, default='0')
    modafanil = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    metformin = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')
    expedited_shipping = models.CharField(max_length=255, choices=YES_NO_CHOICES, default='No')





















    def __str__(self):
        return str(self.patient.first_name)

