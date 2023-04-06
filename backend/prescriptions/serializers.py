from rest_framework import serializers
from .models import Prescription, PatientInformation, DoctorInformation, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInformation
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInformation
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
