# Generated by Django 3.2.11 on 2022-04-28 07:24

from django.db import migrations
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0002_auto_20220413_1308'),
        ('recuit', '0017_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='my_state_field',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.state'),
        ),
    ]
