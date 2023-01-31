# Generated by Django 4.1.5 on 2023-01-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0017_alter_medicationorder_sermorelin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientorder',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Filled', 'Filled'), ('Archived', 'Archived'), ('Requested', 'Requested')], default='Pending', max_length=255),
        ),
    ]
