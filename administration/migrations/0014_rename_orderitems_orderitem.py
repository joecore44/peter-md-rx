# Generated by Django 4.1.5 on 2023-01-26 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0013_provider_patientorder_orderitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]
