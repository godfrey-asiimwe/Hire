from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db.models import Q, F
from django.shortcuts import render, redirect

from django.contrib import messages
import datetime
from .forms import NewUserForm, UserProfileForm, JobPositionForm

# Create your views here.
from .models import Job, YearOfExp, salaryScale, EducationLevel, JobType, UserProfile, Applications, JobPosition


def Dashboard(request):
    today = datetime.datetime.today()
    jobs = Job.objects.all().annotate(odd=F('id') % 2).filter(odd=True, deadline__gt=today).order_by("-id")
    job2s = Job.objects.all().annotate(odd=F('id') % 2).filter(odd=False, deadline__gt=today).order_by("-id")

    context = {'jobs': jobs, 'job2s': job2s}
    return render(request, 'landingPage.html', context)


def Dashboard2(request):
    today = datetime.datetime.today()
    jobs = Job.objects.all().filter(deadline__gt=today)
    applications = Applications.objects.all().count()
    totalJobs = Job.objects.all().count()

    to_be_deleted = []
    for job in jobs:

        if not Applications.objects.filter(job=job,
                                           user=request.user).exists():

            to_be_deleted.append(job.id)

            jobs.exclude(id__in=to_be_deleted)
        else:
            print('false')

    context = {'jobs': jobs, 'applications': applications, 'totalJobs': totalJobs}
    return render(request, 'Dashboard2.html', context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')

    form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_request(request):
    logout(request)
    return redirect("login")


def register_request(request):
    return render(request=request, template_name="addMember.html")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile()
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/profile/' + str(request.user.id))
        else:
            messages.error(request,
                           form.errors)
    form = NewUserForm
    return render(request, 'register.html', context={"register_form": form})


def reg_success(request):
    return render(request, 'reg_success.html')


def log_success(request):
    return render(request, 'login_success.html')


def logout_request(request):
    logout(request)
    return redirect("/")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
        else:
            messages.error(request,
                           'Login unsuccessful, Check your information and try again')

    form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def Profile(request, id):
    userProfile = UserProfile.objects.get(user=request.user)

    years = YearOfExp.objects.all().order_by("-created")
    salaryScales = salaryScale.objects.all().order_by("-created")
    EducationLevels = EducationLevel.objects.all().order_by("-created")
    JobTypes = JobType.objects.all().order_by("-created")

    context = {'years': years, 'salaryScales': salaryScales, 'EducationLevels': EducationLevels, 'JobTypes': JobTypes,
               'userProfile': userProfile}
    return render(request, 'profile.html', context)


def updateProfile(request, id):
    userProfile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(request.POST, request.FILES, instance=userProfile)

    if form.is_valid():
        form.save()
        return redirect("/profile/" + str(request.user.id))
    else:
        messages.error(request, form.errors)
    return render(request, 'profile.html', {'userProfile': userProfile})


def JobApplications(request, id):
    application = Applications()
    job = Job.objects.get(id=id)
    application.user = request.user
    application.job = job

    userProfile = UserProfile.objects.get(user=request.user)

    if userProfile.jobType is None:
        # application.save()
        messages.error(request, "Update your Profile and apply again")
        return redirect("/profile/" + str(request.user.id))
    else:
        if userProfile.name is None:
            messages.error(request, "Update your Profile and apply again")
            return redirect("/profile/" + str(request.user.id))
        else:
            if userProfile.educationLevel is None:
                messages.error(request, "Update your Profile and apply again")
                return redirect("/profile/" + str(request.user.id))
            else:
                if userProfile.salaryScale is None:
                    messages.error(request, "Update your Profile and apply again")
                    return redirect("/profile/" + str(request.user.id))
                else:
                    if userProfile.yearOfExp is None:
                        messages.error(request, "Update your Profile and apply again")
                        return redirect("/profile/" + str(request.user.id))
                    else:
                        if userProfile.upload is None:
                            messages.error(request, "Update your Profile and apply again")
                            return redirect("/profile/" + str(request.user.id))
                        else:
                            application.save()
                            messages.success(request, "You have seccessfully Apllied for the Job, wait for feedback")
                            return redirect("/applied")

    return redirect("/dashboard")


def JobAppliedFor(request):
    applications = Applications.objects.all().filter(user=request.user)
    context = {'applications': applications}
    return render(request, 'appliedFor.html', context)


def activeJobs(request):
    today = datetime.datetime.today()

    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            jobs = Job.objects.filter(name__contains=query_name)
            return render(request, 'activeJobs.html', {"jobs": jobs})
    else:
        jobs = Job.objects.all().filter(deadline__gt=today)

    context = {'jobs': jobs}
    return render(request, 'activeJobs.html', context)


def expiredJobs(request):
    today = datetime.datetime.today()
    jobs = Job.objects.all().filter(deadline__lt=today)
    context = {'jobs': jobs}
    return render(request, 'activeJobs.html', context)


def activeApps(request):
    today = datetime.datetime.today()
    jobs = Job.objects.all().filter(deadline__gt=today)

    context = {'jobs': jobs}
    return render(request, 'applicants.html', context)


def expiredApps(request):
    today = datetime.datetime.today()
    jobs = Job.objects.all().filter(deadline__lt=today)

    context = {'jobs': jobs}
    return render(request, 'applicants.html', context)


def showApplicants(request, id):
    applications = Applications.objects.filter(job=id)

    job = Job.objects.get(id=id)

    userprofile = []
    for applicant in applications:
        userprofile += UserProfile.objects.filter(user=applicant.user).order_by("yearOfExp")

    context = {'applications': applications, 'job': job, 'userprofile': userprofile}
    return render(request, 'viewApplicants.html', context)


def showSortedApplicants(request, id):
    applications = Applications.objects.filter(job=id)

    job = Job.objects.get(id=id)

    userprofile = []
    for applicant in applications:
        userprofile += UserProfile.objects.filter(user=applicant.user, jobType=job.jobType).order_by("-educationLevel")

    context = {'applications': applications, 'job': job, 'userprofile': userprofile}
    return render(request, 'SortedList.html', context)


def JobDetail(request, id):
    job = Job.objects.get(id=id)

    context = {'job': job}
    return render(request, 'JobDetail.html', context)


def CreatePosition(request):
    form = JobPositionForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Saved")
        redirect('/positions')
    else:
        JobPositionForm()
    context = {}
    return render(request, 'position.html', context)


def DisplayPositions(request):
    positions = JobPosition.objects.all()

    context = {'positions': positions}
    return render(request, 'positions.html', context)
