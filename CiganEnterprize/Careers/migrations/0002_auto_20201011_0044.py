# Generated by Django 3.0.8 on 2020-10-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Careers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableinternship',
            name='representation_image',
            field=models.ImageField(default='default.jpg', upload_to='internship_representation_images/'),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='representation_image',
            field=models.ImageField(default='default.jpg', upload_to='jobs_representation_images/'),
        ),
    ]
