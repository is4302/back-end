from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, UserManager

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

# class DoctorRegistrationSerializer(RegisterSerializer):
#     account = serializers.PrimaryKeyRelatedField(read_only=True)
#     hospital_name = serializers.CharField(max_length=255)

#     def get_cleaned_data(self):
#         data_dict = super().get_cleaned_data()
#         extra_data = {
#             'hospital_name': self.validated_data.get('hospital_name', ''),
            
#         }
#         data_dict.update(extra_data)
#         return data_dict

#     def save(self, request):
#         user = super(DoctorRegistrationSerializer, self).save(request)
#         user.is_doctor = True
#         user.save()
#         doctor_profile = DoctorInformation(user=user, hospital_name=self.validated_data.get('hospital_name', ''))
#         doctor_profile.save()
#         return user