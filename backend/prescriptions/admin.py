from django.contrib import admin
from .models import Prescription, PatientInformation, DoctorInformation

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'doctor_id', 'prescription_desc', 'hash_id')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'height', 'weight', 'history', 'allergies', 'patient_id')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital_name', 'doctor_id')

# Register your models here.
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PatientInformation, PatientAdmin)
admin.site.register(DoctorInformation, DoctorAdmin)