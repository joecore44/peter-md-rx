from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PatientProfile, MedicationOrder

@receiver(post_save, sender=PatientProfile)
def create_patient_profile(sender, instance, created, **kwargs):
    if created:
        MedicationOrder.objects.create(patient=instance)
