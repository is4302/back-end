from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer
from .models import Prescription, PatientInformation, DoctorInformation
# Create your views here.

class PrescriptionView(viewsets.ModelViewSet):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = PatientInformation.objects.all()

class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = DoctorInformation.objects.all()
