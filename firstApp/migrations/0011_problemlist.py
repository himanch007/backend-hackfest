# Generated by Django 3.2.9 on 2022-01-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0010_delete_problemlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='problemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosisName', models.CharField(max_length=100)),
                ('bodySite', models.CharField(max_length=100)),
                ('dateOfOnset', models.DateField()),
                ('severity', models.CharField(max_length=100)),
                ('diagnosticCertainity', models.CharField(max_length=100)),
                ('patient_id', models.IntegerField()),
            ],
        ),
    ]
