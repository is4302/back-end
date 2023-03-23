from rest_framework import serializers
from .models import Prescription, PatientInformation, DoctorInformation

class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = ('id', 'patient_id', 'doctor_id', 'prescription_desc', 'hash_id')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInformation
        fields = ('id', 'name', 'dob', 'height', 'weight', 'history', 'allergies', 'patient_id')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInformation
        fields = ('id', 'name', 'hospital_name', 'doctor_id')
