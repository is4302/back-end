from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'height', 'weight', 'history', 'allergies', 'patient_wallet')
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital_name', 'doctor_wallet')
    
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('rand_id', 'date', 'diagnosis', 'treatment', 'patient', 'doctor')

class ApptAdmin(admin.ModelAdmin):
    list_display = ('appointment_time', 'patient', 'doctor')

class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'email', 'wallet_address', 'is_patient', 'is_doctor', 'is_superuser', 'is_staff')
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ['name', 'email', 'wallet_address', 'is_patient', 'is_doctor', 'is_superuser', 'is_staff']
        },),
    ]
    fieldsets = [
        (None, {
            'fields': ['name', 'email', 'wallet_address','is_patient', 'is_doctor', 'is_superuser', 'is_staff']
        },),
    ]
    ordering = ('name',)



# Register your models here.
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PatientInformation, PatientAdmin)
admin.site.register(DoctorInformation, DoctorAdmin)
admin.site.register(Appointment, ApptAdmin)
admin.site.register(User, CustomUserAdmin)