from django import forms
from django.forms import ModelForm
from .models import Owner, Patient, Appointment

# CRUD - Create
class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('pet_name', 'animal_type', 'breed', 'age', 'owner')

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'day', 'time')
        widgets = {
            'day': DateInput(),
            'time': TimeInput()
        }

#CRUD - Update
class OwnerUpdateForm(forms.ModelForm):
    #form for updating owners
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)

class PatientUpdateForm(forms.ModelForm):
    #form for updating patients
    class Meta:
        model = Patient
        fields = ('pet_name', 'animal_type', 'breed', 'age', 'owner')

class DateInput(forms.DateInput):
    input_type = 'date'
class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'day', 'time')
        widgets = {
            'day': DateInput(),
        }