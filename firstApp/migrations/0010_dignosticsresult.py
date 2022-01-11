# Generated by Django 3.2.8 on 2022-01-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0009_delete_dignosticsresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='dignosticsresult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('test_result', models.CharField(max_length=50)),
                ('patient_id', models.IntegerField()),
            ],
        ),
    ]
