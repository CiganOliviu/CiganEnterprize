# Generated by Django 3.0.8 on 2020-09-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0004_auto_20200915_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaiblejob',
            name='job_type',
            field=models.CharField(choices=[('Remote', 'Remote'), ('Non-Remote', 'Non-Remote')], default='Non-Remote', max_length=100),
        ),
    ]
