from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from patient_app.models import Patient, Doctor

class PatientRegistrationSerializer(RegisterSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    dob = serializers.DateField()
    height = serializers.IntegerField()
    weight = serializers.FloatField()
    history = serializers.JSONField()
    allergies = serializers.CharField()
    patient_wallet = serializers.CharField()

    def get_cleaned_data(self):
        data = super(PatientRegistrationSerializer, self).get_cleaned_data()
        extra = {
            'name': self.validated_data.get('name', ''),
            'dob': self.validated_data.get('dob', ''),
            'height': self.validated_data.get('height', ''),
            'weight': self.validated_data.get('weight', ''),
            'history': self.validated_data.get('history', ''),
            'allergies': self.validated_data.get('allergies', ''),
            'patient_wallet': self.validated_data.get('patient_wallet', ''),
        }
        data.update(extra)
        return data
    
    def save(self, request):
        user = super(PatientRegistrationSerializer, self).save(request)
        user.is_patient = True
        user.save()
        patient = Patient(patient=user, name=self.cleaned_data.get('name'), dob=self.cleaned_data.get('dob'),
                          height=self.cleaned_data.get('height'), weight=self.cleaned_data.get('weight'),
                          history=self.cleaned_data.get('history'), allergies=self.cleaned_data.get('allergies'),
                          patient_wallet=self.cleaned_data.get('patient_wallet'))
        patient.save()
        return user
    
class DoctorRegistrationSerializer(RegisterSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    hospital_name = serializers.CharField()
    doctor_wallet = serializers.CharField()

    def get_cleaned_data(self):
        data = super(DoctorRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
            'hospital_name': self.validated_data.get('hospital_name', ''),
            'doctor_wallet': self.validated_data.get('doctor_wallet', '')
        }
        data.update(extra_data)
        return data
    
    def save(self, request):
        user = super(DoctorRegistrationSerializer, self).save(request)
        user.is_doctor = True
        user.save()
        doctor = Doctor(doctor=user, name=self.cleaned_data.get('name'), hospital_name=self.cleaned_data.get('hospital_name'),
                        doctor_wallet=self.cleaned_data.get('doctor_wallet'))
        doctor.save()
        return user

