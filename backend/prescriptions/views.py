from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer, AppointmentSerializer
from .serializers import PatientRegistrationSerializer, DoctorRegistrationSerializer, UserLoginSerializer, AppointmentCreationSerializer, PrescriptionCreationSerializer
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your views here.
import traceback


class PatientRegistrationView(APIView):
    serializer_class = PatientRegistrationSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        response = {'success': 'True', 'message': 'Patient registered'}
        return Response(response, status=status.HTTP_201_CREATED)


class DoctorRegistrationView(APIView):
    serializer_class = DoctorRegistrationSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception:
            print(traceback.format_exc())
            raise Exception

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
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token': serializer.data['token'],
            'is_doctor': serializer.data['is_doctor'],
            'is_patient': serializer.data['is_patient']
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
                        'height': profile.height,
                        'weight': profile.weight,
                        'history': profile.history,
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
                        'hospital': profile.hospital_name,
                        'wallet': profile.doctor_wallet
                    }]
                }
            if user.is_superuser:
                profile = User.objects.get(user=user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'true',
                    'status': status.HTTP_200_OK,
                    'message': 'Admin Profile retrieved',
                    'data': [{
                        'name': profile.name,
                        'email': profile.email,
                        'wallet': profile.wallet_address
                    }]
                }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'User not found',
                'error': str(e)
            }

        return Response(response, status=status_code)


class PrescriptionView(APIView):
    serializer_classes = (PrescriptionCreationSerializer,
                          PrescriptionSerializer)
    queryset = Prescription.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = request.user
        if user.is_doctor:
            serializer = self.serializer_classes[0](data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.validated_data['doctor'].user != request.user:
                response = {
                    'success': 'false', 'message': 'You cannot prescribe medicine on behalf of other doctor'}
                return Response(response, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            response = {'success': 'true', 'message': 'Medicine prescribed'}
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)
        else:
            response = {'success': 'false',
                        'message': 'Only doctors can prescribe medicine'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def get(self, request):
        try:
            user = request.user
            if user.is_patient:
                status_code = status.HTTP_200_OK
                profile = PatientInformation.objects.get(user=user)
                appt = Prescription.objects.filter(
                    patient__patient_wallet=profile.patient_wallet)
                serialized = self.serializer_classes[1](list(appt), many=True)
                return Response(serialized.data, status=status_code)
            if user.is_doctor:
                status_code = status.HTTP_200_OK
                profile = DoctorInformation.objects.get(user=user)
                appt = Prescription.objects.filter(
                    doctor__doctor_wallet=profile.doctor_wallet)
                serialized = self.serializer_classes[1](data=appt, many=True)
                return Response(serialized.data, status=status_code)

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'User not found',
                'error': str(e)
            }
            return Response(response, status=status_code)


class AppointmentView(APIView):
    serializer_class = AppointmentCreationSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if (serializer.validated_data['patient'].user != request.user) and (serializer.validated_data['doctor'].user != request.user):
            return Response({'success': 'false', 'message': 'You cannot create an appointment for someone else'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        response = {'success': 'true', 'message': 'Appointment set'}
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

    def get(self, request):
        try:
            user = request.user
            if user.is_patient:
                status_code = status.HTTP_200_OK
                profile = PatientInformation.objects.get(user=user)
                appt = Appointment.objects.filter(patient=profile)
                serialized = AppointmentSerializer(list(appt), many=True)
                # if serialized.is_valid(raise_exception=True):
                return Response(serialized.data, status=status_code)
            if user.is_doctor:
                status_code = status.HTTP_200_OK
                profile = DoctorInformation.objects.get(user=user)
                appt = Appointment.objects.filter(doctor=profile)
                serialized = AppointmentSerializer(list(appt), many=True)
                # if serialized.is_valid():
                return Response(serialized.data, status=status_code)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Error occured',
                'error': str(e)
            }

        return Response(response, status=status_code)

class AppointmentGetDoctorView(APIView):
    queryset = Appointment.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request):
        doctor = request.query_params.get("doctor_wallet")
        queryset_list = Appointment.objects.filter(
            doctor__doctor_wallet=doctor)
        if queryset_list:
            serialized = AppointmentSerializer(data=queryset_list, many=True)
            serialized.is_valid()
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)

class GetDoctorView(APIView):
    queryset = DoctorInformation.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        query_list = DoctorInformation.objects.all()
        if query_list:
            serialized = DoctorSerializer(data=query_list, many=True)
            serialized.is_valid()
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            response = {
                'success': 'false',
                'message': 'No doctors registered on this platform'
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
