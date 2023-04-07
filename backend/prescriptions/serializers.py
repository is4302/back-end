from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class UserSeralizerToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('token', 'email', 'password', 'profile')

    def get_token(self, response): ##use to get user
        payload = jwt_payload_handler(response)
        token = jwt_encode_handler(payload) 
        return token
    
    def create(self, data):
        profile = data.pop('profile')
        user = User.objects.create_user(**data)
        PatientInformation.objects.create(
            user=user,
            name=profile['name'],
            dob=profile['dob'],
            height=profile['height'],
            weight=profile['weight'],
            history=profile['history'],
            allergies=profile['allergies'],
            patient_wallet=profile['patient_wallet']
        )
        user.save()
        return user


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'