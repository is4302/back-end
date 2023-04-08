from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInformation
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInformation
        fields = '__all__'

class PatientRegistrationSerializer(serializers.ModelSerializer):
    profile = PatientSerializer(required=False)

    class Meta:
        model = User
        fields = ('name', 'email', 'wallet_address', 'password', 'profile')

    def create(self, data):
        profile_data = data.pop('profile')
        user = User.objects.create_patient(**data)
        PatientInformation.objects.create_patient(
            user = user,
            dob = profile_data['dob'],
            height = profile_data['height'],
            weight = profile_data['weight'],
            history = profile_data['history'],
            allergies = profile_data['allergies']
        )
        return user

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    profile = DoctorSerializer(required=False)

    class Meta:
        model = User
        fields = ('name', 'email', 'wallet_address', 'password', 'profile')

    def create(self, data):
        profile_data = data.pop('profile')
        user = User.objects.create_doctor(**data)
        DoctorInformation.create(
            user = user,
            hospital_name = profile_data['hospital_name']
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)


    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('No email or password matched')
        
        try:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        return {'name': user.name, 'email': user.email, 'wallet': user.wallet_address, 'token': token}



class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'