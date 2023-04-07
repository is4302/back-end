from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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

    def get(self, request):
        detail = [ {
            "id": detail.id,
            "date":detail.date,
            "patient": detail.patient, 
            "doctor": detail.doctor,
            "diagnosis": detail.diagnosis,
            "treatment": detail.treatment,
            "rand_id":detail.rand_id
        } for detail in queryset]
        return Response(detail)

    def post(self, request):
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
