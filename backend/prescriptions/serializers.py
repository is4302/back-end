from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User


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
        PatientInformation.objects.create(
            user = user,
            name=profile_data['name'],
            dob = profile_data['dob'],
            height = profile_data['height'],
            weight = profile_data['weight'],
            history = profile_data['history'],
            allergies = profile_data['allergies'],
            patient_wallet = profile_data['patient_wallet']
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
        DoctorInformation.objects.create(
            user = user,
            name = profile_data['name'],
            hospital_name = profile_data['hospital_name'],
            doctor_wallet = profile_data['doctor_wallet']
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    is_patient = serializers.BooleanField(read_only=True, allow_null=True)
    is_doctor = serializers.BooleanField(read_only=True, allow_null=True)


    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('No email or password matched')
        
        try:
            refresh = RefreshToken.for_user(user)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        return {'name': user.name, 'email': user.email, 'wallet': user.wallet_address, 'token':refresh.access_token}


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
