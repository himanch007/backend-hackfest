# Generated by Django 3.2.8 on 2022-01-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_rename_patientmedicalsummary_medicalsummary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='medicalsummary',
        ),
    ]
