from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from patient_app.serializers import PatientRegistrationSerializer, DoctorRegistrationSerializer

# Create your views here.
class PatientRegistrationView(RegisterView):
    serializer_class = PatientRegistrationSerializer

class DoctorRegistrationView(RegisterView):
    serializer_class = DoctorRegistrationSerializer