# Generated by Django 3.2.8 on 2022-01-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_rename_medicalsummary_patientmedicalsummary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='patientmedicalsummary',
            new_name='medicalsummary',
        ),
    ]
