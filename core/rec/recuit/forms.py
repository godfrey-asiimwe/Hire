from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your forms here.
from .models import UserProfile, JobPosition, Job, BioData, interview


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["name", "country", "city", "phone", "yearOfExp", "salaryScale", "educationLevel", "jobType",
                  "upload", ]


class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = ["date", "project", "title", "quantity", "description", "startDate", "endDate", "attachment"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["jobPosition","jobType","yearOfExp","salaryScale","educationLevel","name","description","activities","requirements","deadline"]


class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioData
        fields = ["surname", "othername", "gender", "nationalId", "country", "district", "subCounty", "village",
                  "maritalStatus","residenceStatus","dob", ]


class InterviewDataForm(forms.ModelForm):
    class Meta:
        model = interview
        fields = ["userprofile","questions", "mark",]
