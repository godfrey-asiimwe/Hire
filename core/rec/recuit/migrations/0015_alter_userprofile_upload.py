# Generated by Django 3.2.4 on 2022-04-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuit', '0014_alter_userprofile_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]
