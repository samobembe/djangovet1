from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Owner, Patient, Appointment
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm, AppointmentCreateForm, AppointmentUpdateForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
   context = {
   "login_view": "active"
   }
   if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
   if user is not None:
      login(request, user)
      return redirect("home")
   else:
      return HttpResponse("invalid credentials")
   return render(request, "registration/login.html", context)

def logout_view(request):
   logout(request)
   return redirect("home")

@login_required
def home(request):
   context = {"name": "<Put your name here>"}
   return render(request, "vetoffice/home.html", context)

class SignUp(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'

# CRUD - (R)ead
class OwnerList(LoginRequiredMixin,ListView):
   model = Owner

class PatientList(LoginRequiredMixin,ListView):
   model = Patient

# CRUD - (C)reate
class OwnerCreate(LoginRequiredMixin,CreateView):
   model = Owner
   template_name = "vetoffice/owner_create_form.html"
   form_class = OwnerCreateForm

class PatientCreate(LoginRequiredMixin,CreateView):
   model=Patient
   template_name = "vetoffice/patient_create_form.html"
   form_class = PatientCreateForm

# CRUD - (U)pdate
class OwnerUpdate(LoginRequiredMixin,UpdateView):
   model = Owner
   template_name = "vetoffice/owner_update_form.html"
   form_class = OwnerUpdateForm

class PatientUpdate(LoginRequiredMixin,UpdateView):
   model = Patient
   template_name = "vetoffice/patient_update_form.html"
   form_class = PatientUpdateForm

# CRUD - (D)elete
class OwnerDelete(LoginRequiredMixin,DeleteView):
   model = Owner
   template_name = "vetoffice/owner_delete_form.html"
   success_url = "/owner/list"

class PatientDelete(LoginRequiredMixin,DeleteView):
   model = Patient
   template_name = "vetoffice/patient_delete_form.html"
   success_url = "/patient/list"
