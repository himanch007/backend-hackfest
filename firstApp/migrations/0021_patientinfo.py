# Generated by Django 3.2.9 on 2022-01-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0020_alter_medicalsummary_expire'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('patient_id', models.IntegerField()),
            ],
        ),
    ]
