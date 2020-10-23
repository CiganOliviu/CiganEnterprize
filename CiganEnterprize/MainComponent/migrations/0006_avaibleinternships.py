# Generated by Django 3.0.8 on 2020-09-27 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0005_avaiblejob_job_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaibleInternships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
                ('requirements', models.TextField(default='')),
                ('one_day', models.TextField(default='')),
                ('released_day', models.DateTimeField(auto_now_add=True)),
                ('job_slug', models.SlugField(default='', max_length=200, unique=True)),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.Studio')),
            ],
        ),
    ]
