# Generated by Django 3.0.8 on 2020-10-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communication', '0004_auto_20201010_1703'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyRespond',
        ),
        migrations.AddField(
            model_name='contact',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
