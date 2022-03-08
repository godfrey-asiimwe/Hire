from django.contrib import admin
# Register your models here.
# Register your models here.

from .models import JobType, Job, salaryScale, YearOfExp, EducationLevel


class jobType(admin.ModelAdmin):
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


admin.site.register(JobType, jobType)
admin.site.register(Job, job)
admin.site.register(salaryScale, salaryscale)
admin.site.register(YearOfExp, Yearofexp)
admin.site.register(EducationLevel,educationLevel)