# Generated by Django 3.2.11 on 2022-07-06 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recuit', '0022_job_jobposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('othername', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('nationalId', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('subCounty', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('maritalStatus', models.CharField(max_length=50)),
                ('residenceStatus', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
