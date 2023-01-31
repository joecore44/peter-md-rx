# Generated by Django 4.1.5 on 2023-01-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_alter_medicationorder_enclomiphene'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationorder',
            name='gonadorelin_nasal',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='bpc_157',
            field=models.CharField(choices=[('0', '0'), ('1', '1 Month $226'), ('2', '2 Month $400'), ('3', '3 Month $600')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='bpc_157_c',
            field=models.CharField(choices=[('0', '0'), ('1', '1 Month $180'), ('2', '2 Month $348'), ('3', '3 Month $511')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='dhea',
            field=models.CharField(choices=[('0', '0'), ('10', '10 Tablets: $40'), ('15', '15 Tablets: $60'), ('20', '20 Tablets: $75'), ('30', '30 Tablets: $113')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='finasteride',
            field=models.CharField(choices=[('0', '0'), ('30', '30 Tablets: $40'), ('60', '60 Tablets: $74')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='ipa',
            field=models.CharField(choices=[('0', '0'), ('1', '1 Month $255'), ('2', '2 Month $430'), ('3', '3 Month $635')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='ipa_cjc',
            field=models.CharField(choices=[('0', '0'), ('1', '1 Month $255'), ('2', '2 Month $430'), ('3', '3 Month $635')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='mic_oral',
            field=models.CharField(choices=[('0', '0'), ('30', 'One Month: 30 tablets $86.50'), ('60', 'Two Months: 60 tablets $163.50'), ('90', 'Three Months: 90 tablets $241.50')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='mk_677',
            field=models.CharField(choices=[('0', '0'), ('1', '1 Month $195'), ('2', '2 Month $380'), ('3', '3 Month $570')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='pregnelone',
            field=models.CharField(choices=[('0', '0'), ('30', '30 Tablets: $79'), ('60', '60 Tablets: $149')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='sermorelin_p',
            field=models.CharField(choices=[('0', '0'), ('1', '1 Month $183'), ('2', '2 Month $355'), ('3', '3 Month $530')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='sildenafil',
            field=models.CharField(choices=[('0', '0'), ('10', '10 Tablets: $62.50'), ('15', '15 Tablets: $90'), ('20', '20 Tablets: $120'), ('30', '30 Tablets: $180')], default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='medicationorder',
            name='tadalafil',
            field=models.CharField(choices=[('0', '0'), ('10', '10 Tablets: $72.50'), ('15', '15 Tablets: $100'), ('20', '20 Tablets: $140'), ('30', '30 Tablets: $210')], default='0', max_length=25),
        ),
    ]
