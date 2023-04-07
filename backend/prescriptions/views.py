from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer, AppointmentSerializer
from .models import Prescription, PatientInformation, DoctorInformation, Appointment
from django.contrib.auth import get_user_model
User = get_user_model()
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

class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            is_patient = data['is_patient']
            if is_patient == 'True':
                is_patient = True
                dob = data['dob']
                height = data['height']
                weight = data['weight']
                history = data['history']
                allergies = data['allergies']
            else:
                is_patient = False
                hospital_name = data['hospital_name']
            
            if not User.objects.filter(email=email).exists():
                if is_patient:
                    User.objects.create_patient(name = name, email = email, password = password, dob = dob, height = height, weight = weight, history = history, allergies = allergies)
                    return Response(
                        {'success': 'Patient created Sucessfully.'},
                        status=status.HTTP_201_CREATED
                    )
                else:
                    User.objects.creete_doctor(name = name, email = email, password = password, hospital_name = hospital_name)
                    return Response(
                        {'success': 'Doctor created sucessfully.'},
                        status=status.HTTP_201_CREATED
                    )
            else:
                return Response({'error': 'User with this email already exists.'},
                                status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {'error': e},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
