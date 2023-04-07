from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'wallet_address', 'dob', 'height', 'weight', 'history', 'allergies')

    def name(self, obj):
        return obj.user.name
    def email(self, obj):
        return obj.user.email
    def wallet_address(self, obj):
        return obj.user.wallet_address
    

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'wallet_address', 'hospital_name')
    
    def name(self, obj):
        return obj.user.name
    def email(self, obj):
        return obj.user.email
    def wallet_address(self, obj):
        return obj.user.wallet_address

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
            'fields': ['name', 'email', 'wallet_address', 'is_patient', 'is_doctor', 'is_superuser', 'is_staff']
        },),
    ]
    ordering = ('name',)



# Register your models here.
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PatientInformation, PatientAdmin)
admin.site.register(DoctorInformation, DoctorAdmin)
admin.site.register(Appointment, ApptAdmin)
admin.site.register(User, CustomUserAdmin)