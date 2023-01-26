# Generated by Django 4.1.5 on 2023-01-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_alter_medicationorder_testosterone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationorder',
            name='testosterone',
            field=models.CharField(choices=[('IM', 'IM (intramuscular) - injecting into the muscle'), ('SUBQ', 'SUBQ (Subcutaneous) - injecting into the fatty tissue'), ('NA', 'Not due for testosterone to be filled'), ('ENCLOMIPHENE', 'Enclomophine - Clomid')], default='NA', max_length=255),
        ),
    ]
