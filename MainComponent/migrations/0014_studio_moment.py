# Generated by Django 3.0.8 on 2020-09-28 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0013_remove_studio_moment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='moment',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 21, 19, 59, 497476)),
        ),
    ]