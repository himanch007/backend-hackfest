# Generated by Django 3.2.8 on 2022-01-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0019_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalsummary',
            name='expire',
            field=models.CharField(max_length=100),
        ),
    ]