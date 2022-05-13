from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Dashboard, name='dashboard'),
    path('login',views.login_request, name='login'),
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
    path('sortedList/<int:id>',views.showSortedApplicants,name="showSortedApplicants"),
    path('detail/<int:id>', views.JobDetail),
    path('position/',views.DisplayPositions),
    path('papprove/', views.DisplayPositionForApproval),
    path('approveHr/<int:id>', views.approvePositionHR),
    path('cmapprove/', views.DisplayPositionForCMApproval),
    path('approveCM/<int:id>', views.approvePositionCM),
    path('addPosition/',views.CreatePosition, name="addPosition"),

]