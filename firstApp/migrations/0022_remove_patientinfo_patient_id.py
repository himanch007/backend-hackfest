# Generated by Django 3.2.8 on 2022-01-14 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0021_patientinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinfo',
            name='patient_id',
        ),
    ]
