# Generated by Django 4.1.5 on 2023-01-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_alter_medicationorder_testosterone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Pending', 'Pending'), ('New Submission', 'New Submission'), ('Active', 'Active')], default='Pending', max_length=255),
        ),
    ]