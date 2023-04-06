from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer, AppointmentSerializer
from .models import Prescription, PatientInformation, DoctorInformation, Appointment
# Create your views here.

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = PatientInformation.objects.all()

class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = DoctorInformation.objects.all()

class PrescriptionView(viewsets.ModelViewSet):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
