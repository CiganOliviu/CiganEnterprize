# Generated by Django 3.0.8 on 2020-09-07 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainView', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sedium_posts', to='MainView.Sedium'),
        ),
    ]
