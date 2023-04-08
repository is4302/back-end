from django.urls import path
from patient_app.views import PatientRegistrationView, DoctorRegistrationView

urlpatterns = [
    path('registration/patient', PatientRegistrationView.as_view(), name='patient-registration'),
    path('registration/doctor', DoctorRegistrationView.as_view(), name='doctor-registration')
]