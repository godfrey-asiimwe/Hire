from django.contrib import admin
# Register your models here.
# Register your models here.
from django.forms import models
from django.forms.widgets import Textarea

from .models import JobType, Job, salaryScale, YearOfExp, EducationLevel, UserProfile, MyModel, JobPosition, \
    ContractType, BioData, Questions, QunHeader, interview


class jobType(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    search_fields = ['name']


class contractType(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    search_fields = ['name']


class Yearofexp(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    search_fields = ['name']


class salaryscale(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    search_fields = ['name']


class educationLevel(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    search_fields = ['name']


class job(admin.ModelAdmin):
    list_display = (
        'jobType', 'name', 'description', 'activities', 'requirements', 'deadline', 'status', 'created_on',
        'updated_on')
    search_fields = ['name']


class userProfile(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone', 'country', 'city')


class jobPosition(admin.ModelAdmin):
    list_display = (
        'date', 'project', 'requestedBy', 'contractType', 'title', 'quantity', 'startDate', 'endDate', 'GradeStep',
        'salaryRange', 'proposed', 'description', 'hr', 'cm')


class bioData(admin.ModelAdmin):
    list_display = ("surname", "othername", "gender", "nationalId", "country", "district", "subCounty", "village",
                    "maritalStatus", "residenceStatus", "dob")


class questions(admin.ModelAdmin):
    list_display = ("question", "answer")


class qunHeader(admin.ModelAdmin):
    list_display = ("name", "description")


class interviews(admin.ModelAdmin):
    list_display = ("job", "userprofile", "questions", "mark", "interviewer")


class myModel(admin.ModelAdmin):
    list_display = ()


admin.site.register(MyModel, myModel)
admin.site.register(JobType, jobType)
admin.site.register(Job, job)
admin.site.register(salaryScale, salaryscale)
admin.site.register(YearOfExp, Yearofexp)
admin.site.register(EducationLevel, educationLevel)
admin.site.register(UserProfile, userProfile)
admin.site.register(JobPosition, jobPosition)
admin.site.register(ContractType, contractType)
admin.site.register(BioData, bioData)
admin.site.register(Questions, questions)
admin.site.register(QunHeader, qunHeader)
admin.site.register(interview, interviews)
