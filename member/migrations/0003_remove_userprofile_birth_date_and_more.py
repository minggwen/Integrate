# Generated by Django 4.2.3 on 2023-08-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_userprofile_birth_date_userprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
    ]