# Generated by Django 4.1.5 on 2023-01-11 01:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_alter_patientprofile_additional_information_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationOrder',
            fields=[
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('testosterone', models.CharField(choices=[('IM', 'IM (intramuscular) - injecting into the muscle'), ('SUBQ', 'SUBQ (Subcutaneous) - injecting into the fatty tissue'), ('N/A', 'not due for testosterone to be filled'), ('ENCLOMIPHENE', 'Enclomophine - Clomid')], default='N/A', max_length=255)),
                ('medical_requests', models.TextField(verbose_name='Comments or Requests')),
                ('additional_medication', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('signature_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25)),
                ('sharps_container', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25)),
                ('alcohol_prep_boxes', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=3)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.patientprofile')),
            ],
        ),
    ]