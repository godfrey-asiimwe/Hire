# Generated by Django 3.2.11 on 2022-05-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuit', '0019_contracttype_jobposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='GradeStep',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='proposed',
            field=models.CharField(max_length=50, null=True),
        ),
    ]