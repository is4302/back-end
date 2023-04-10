from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer, AppointmentSerializer
from .serializers import PatientRegistrationSerializer, DoctorRegistrationSerializer, UserLoginSerializer, AppointmentCreationSerializer
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your views here.


class PatientRegistrationView(APIView):
    serializer_class = PatientRegistrationSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        response = {'success': 'True', 'message': 'Patient registered'}
        return Response(response, status=status.HTTP_201_CREATED)


class DoctorRegistrationView(APIView):
    serializer_class = DoctorRegistrationSerializer
    permission_classes = [AllowAny, ]
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        response = {'success': 'True', 'message': 'Doctor registered'}
        return Response(response, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.none()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token' : serializer.data['token'],
            'is_doctor' : serializer.data['is_doctor'],
            'is_patient' : serializer.data['is_patient']
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class ProfileView(APIView):

    def get(self, request, format=None):
        try:
            user = request.user
            if user.is_patient:
                #username = User.objects.get(user=user)
                status_code = status.HTTP_200_OK
                profile = PatientInformation.objects.get(user=user)
                response = {
                    'success': 'true',
                    'status': status.HTTP_200_OK,
                    'message': 'Patient Information successfully retrieved',
                    'data': [{
                        'name': profile.name,
                        'dob': profile.dob,
                        'height':profile.height,
                        'weight':profile.weight,
                        'history':profile.history,
                        'allergies': profile.allergies,
                        'wallet': profile.patient_wallet
                    }]
                }
            if user.is_doctor:
                #username = User.objects.get(user=user)
                status_code = status.HTTP_200_OK
                profile = DoctorInformation.objects.get(user=user)
                response = {
                    'success': 'true',
                    'status': status.HTTP_200_OK,
                    'message': 'Doctor Information successfully retrieved',
                    'data': [{
                        'name': profile.name,
                        'hospital':profile.hospital_name,
                        'wallet': profile.doctor_wallet
                    }]
                }
            if user.is_superuser:
                profile = User.objects.get(user = user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'true',
                    'status': status.HTTP_200_OK,
                    'message': 'Admin Profile retrieved',
                    'data': [{
                        'name': profile.name,
                        'email':profile.email,
                        'wallet': profile.wallet_address
                    }]
                }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success':'false',
                'status':status.HTTP_400_BAD_REQUEST,
                'message':'User not found',
                'error': str(e)
            }

        return Response(response, status=status_code)
    
class PrescriptionView(APIView):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

    def post(self, request):
        pass

    def get(self, request):
        pass

class AppointmentView(APIView):
    serializer_class = AppointmentCreationSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': 'true','message': 'Appointment set'}
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


    def get(self, request):
        try:
            user = request.user
            if user.is_patient:
                status_code = status.HTTP_200_OK
                profile = PatientInformation.objects.get(user=user)
                appt = Appointment.objects.filter(patient__patient_wallet=profile.patient_wallet)
                serialized = AppointmentSerializer(data=appt, many=True)
                serialized.is_valid()
                return Response(serialized.data, status=status_code)
            if user.is_doctor:
                status_code = status.HTTP_200_OK
                profile = DoctorInformation.objects.get(user=user)
                appt = Appointment.objects.filter(doctor__doctor_wallet=profile.doctor_wallet)
                serialized = AppointmentSerializer(data=appt, many=True)
                if serialized.is_valid():
                    return Response(serialized.data, status=status_code)
                else:
                    return Response("Disallowed", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success':'false',
                'status':status.HTTP_400_BAD_REQUEST,
                'message':'User not found',
                'error': str(e)
            }

        return Response(response, status=status_code)
