from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class JobType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Job(models.Model):
    jobType = models.ForeignKey(
        JobType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    activities = models.CharField(max_length=50)
    requirements = models.CharField(max_length=50)
    deadline = models.DateField()
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'active'),
        (Inactive_Status, 'unactive'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=Inactive_Status)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class YearOfExp(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class salaryScale(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    jobType = models.ForeignKey(
        JobType, on_delete=models.CASCADE)
    yearOfExp = models.ForeignKey(
        YearOfExp, on_delete=models.CASCADE)
    salaryScale = models.ForeignKey(
        salaryScale, on_delete=models.CASCADE)
    educationLevel = models.ForeignKey(
        EducationLevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Applications(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['job']

    def __str__(self):
        return self.job