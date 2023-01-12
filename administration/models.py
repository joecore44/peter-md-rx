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
            ('N/A', 'not due for testosterone to be filled'),
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
    testosterone = models.CharField(max_length=255, choices=TEST_CHOICES, default='N/A')
    medical_requests = models.TextField(verbose_name='Comments or Requests')
    additional_medication = models.CharField(max_length=255, choices=YES_NO_CHOICES)
    signature_required = models.CharField(max_length=25, choices=YES_NO_CHOICES)
    sharps_container = models.CharField(max_length=25, choices=YES_NO_CHOICES)
    alcohol_prep_boxes = models.CharField(max_length=3, choices=NUMBER_CHOICES)

    def __str__(self):
        return str(self.patient.first_name)

