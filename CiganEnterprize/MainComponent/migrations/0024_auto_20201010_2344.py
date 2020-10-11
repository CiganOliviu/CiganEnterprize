# Generated by Django 3.0.8 on 2020-10-10 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0023_auto_20201010_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availablejob',
            name='location',
        ),
        migrations.RemoveField(
            model_name='internshipsappliance',
            name='career',
        ),
        migrations.RemoveField(
            model_name='jobsappliance',
            name='career',
        ),
        migrations.DeleteModel(
            name='AvailableInternship',
        ),
        migrations.DeleteModel(
            name='AvailableJob',
        ),
        migrations.DeleteModel(
            name='InternshipsAppliance',
        ),
        migrations.DeleteModel(
            name='JobsAppliance',
        ),
    ]