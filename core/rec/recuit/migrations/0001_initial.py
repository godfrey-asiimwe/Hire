# Generated by Django 3.2.11 on 2022-01-15 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('activities', models.CharField(max_length=50)),
                ('requirements', models.CharField(max_length=50)),
                ('deadline', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'unactive')], default=0)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('jobType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recuit.jobtype')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]