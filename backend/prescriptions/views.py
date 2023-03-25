from django.shortcuts import render
from django_nextjs.render import render_nextjs_page_sync
from rest_framework import viewsets
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer
from .models import Prescription, PatientInformation, DoctorInformation
# Create your views here.

def index(request):
    return render_nextjs_page_sync(request)

class PrescriptionView(viewsets.ModelViewSet):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = PatientInformation.objects.all()

class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = DoctorInformation.objects.all()
