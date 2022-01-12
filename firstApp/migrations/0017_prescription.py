# Generated by Django 3.2.8 on 2022-01-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0016_plancare'),
    ]

    operations = [
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_item', models.CharField(max_length=100)),
                ('substance_name', models.CharField(max_length=100)),
                ('form', models.CharField(max_length=100)),
                ('strength', models.FloatField()),
                ('strength_unit', models.CharField(max_length=100)),
                ('route', models.CharField(max_length=100)),
                ('dosage_instructions', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('max_amount', models.FloatField()),
                ('max_amount_dose_unit', models.CharField(max_length=10)),
                ('comments', models.CharField(max_length=100)),
                ('patient_id', models.IntegerField()),
            ],
        ),
    ]