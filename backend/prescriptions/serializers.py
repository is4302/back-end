from rest_framework import serializers
from .models import Prescription, PatientInformation, DoctorInformation, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInformation
        exclude = ['user']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInformation
        exclude = ['user']

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
