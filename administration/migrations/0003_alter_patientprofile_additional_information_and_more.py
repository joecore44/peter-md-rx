# Generated by Django 4.1.5 on 2023-01-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_alter_patientprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='additional_information',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='emergency_contact_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='emergency_contact_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='emergency_contact_relationship',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='zip_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
