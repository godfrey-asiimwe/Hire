# Generated by Django 3.2.11 on 2022-05-05 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recuit', '0020_auto_20220505_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='requestedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]