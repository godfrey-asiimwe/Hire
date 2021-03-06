from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib import admin
from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms.widgets import Textarea
from river.models.fields.state import StateField


class MyModel(models.Model):
    my_state_field = StateField()


class ContractType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class JobType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

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


### Profile
class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    jobType = models.ForeignKey(
        JobType, on_delete=models.CASCADE, null=True)
    yearOfExp = models.ForeignKey(
        YearOfExp, on_delete=models.CASCADE, null=True)
    salaryScale = models.ForeignKey(
        salaryScale, on_delete=models.CASCADE, null=True)
    educationLevel = models.ForeignKey(
        EducationLevel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    upload = models.FileField(upload_to='')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BioData(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    surname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    nationalId = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    subCounty = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    maritalStatus = models.CharField(max_length=50)
    residenceStatus = models.CharField(max_length=50)
    dob = models.DateField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)


class JobPosition(models.Model):
    date = models.DateField()
    project = models.CharField(max_length=50)
    requestedBy = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    contractType = models.ForeignKey(
        ContractType, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    quantity = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    GradeStep = models.CharField(max_length=50, blank=True, null=True)
    salaryRange = models.ForeignKey(
        salaryScale, on_delete=models.CASCADE, null=True)
    proposed = models.CharField(max_length=50, null=True)
    description = RichTextUploadingField()
    attachment = models.FileField(upload_to='')
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'Approved'),
        (Inactive_Status, 'Pending'),
    )
    hr = models.IntegerField(choices=STATUS_CHOICES, default=Inactive_Status)
    cm = models.IntegerField(choices=STATUS_CHOICES, default=Inactive_Status)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Job(models.Model):
    my_state_field = StateField()
    jobPosition = models.ForeignKey(
        JobPosition, on_delete=models.CASCADE)
    jobType = models.ForeignKey(
        JobType, on_delete=models.CASCADE)
    yearOfExp = models.ForeignKey(
        YearOfExp, on_delete=models.CASCADE, null=True)
    salaryScale = models.ForeignKey(
        salaryScale, on_delete=models.CASCADE, null=True)
    educationLevel = models.ForeignKey(
        EducationLevel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()
    activities = RichTextUploadingField()
    requirements = RichTextUploadingField()
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


class QunHeader(models.Model):
    name = RichTextUploadingField()
    description = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Questions(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE)
    header = models.ForeignKey(
        QunHeader, on_delete=models.CASCADE)
    question = RichTextUploadingField()
    answer = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.question


class interview(models.Model):
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)

    job = models.ForeignKey(
        Job, on_delete=models.CASCADE)

    questions = models.ForeignKey(
        Questions, on_delete=models.CASCADE, null=True)

    mark = models.IntegerField(max_length=50)

    interviewer =models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
