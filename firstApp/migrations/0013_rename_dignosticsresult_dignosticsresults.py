# Generated by Django 3.2.8 on 2022-01-12 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0012_dignosticsresult_pasthistory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dignosticsresult',
            new_name='dignosticsresults',
        ),
    ]