from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import PatientInfoForm, ScreenForm
from utils.models_util import compute_eligibility

# Create your views here.
def react(request):
    return render(request, 'ui/react.html')

def patientinfo(request):
    if request.method == "POST":
        form = PatientInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ui/patientinfo.html', {'form': PatientInfoForm(), 'result': 'success'})
    else:
        form = PatientInfoForm()

    return render(request, 'ui/patientinfo.html', {'form': form})

def screen(request):
    if request.method == "POST":
        form = ScreenForm(request.POST)
        if form.is_valid():
            data = form.save()
            eligibility = compute_eligibility(form)
            return render(request, 'ui/screen.html', {'form': form, 'status': eligibility})
    else:
        form = ScreenForm()

    return render(request, 'ui/screen.html', {'form': form})

def dashboard(request):
    return render(request, 'ui/dash.html', {})

    
def zip_analytics(request):
    return render(request, 'ui/zip_analytics.html', {})