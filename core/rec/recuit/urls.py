from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_request, name='login'),
    path('dashboard',views.Dashboard2, name='Dashboard2'),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path('register', views.register_request, name='register'),
    path('reg_success', views.reg_success, name='register'),
    path('profile/<int:id>', views.Profile),
    path('updateprofile/<int:id>', views.updateProfile),
    path('apply/<int:id>', views.JobApplications),
    path('applied/',views.JobAppliedFor),
    path('active/',views.activeJobs),
    path('notactive/',views.expiredJobs),
    path('activeApp/',views.activeApps),
    path('notactiveApp/',views.expiredApps),
    path('viewApplicants/<int:id>', views.showApplicants, name='viewApplicants'),
]