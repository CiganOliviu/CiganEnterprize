# Generated by Django 3.0.8 on 2020-09-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0010_auto_20200927_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaibleinternship',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
