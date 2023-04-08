from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import PrescriptionSerializer, PatientSerializer, DoctorSerializer, AppointmentSerializer, PatientRegistrationSerializer, DoctorRegistrationSerializer, UserLoginSerializer
from .models import Prescription, PatientInformation, DoctorInformation, Appointment, User
# from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
# User = get_user_model()
# Create your views here.


class PatientRegistrationView(CreateAPIView):

    serializer_class = PatientRegistrationSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        response = {'success': 'True', 'message': 'Patient registered'}
        return Response(response, status=status.HTTP_201_CREATED)


class DoctorRegistrationView(CreateAPIView):
    serializer_class = DoctorRegistrationSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
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
            'message': 'User logged in  successfully',
            'token' : serializer.data['token']
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class ProfileView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    # queryset = User.objects.all()

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = queryset.get(pk=self.request.user.id)
    #     self.check_object_permissions(self.request, obj)
    #     return obj

    def get(self, request):

        try:
            if request.user.is_patient:
                user = User.objects.get(user=request.user)
                # username = PatientInformation.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                profile = PatientInformation.objects.get(user=request.user)
                response = {
                    'success': 'true',
                    'status': status.HTTP_200_OK,
                    'message': 'Patient Information successfully retrieved',
                    'data': [{
                        'name': user.name,
                        'dob': profile.dob,
                        'height':profile.height,
                        'weight':profile.weight,
                        'history':profile.history,
                        'allergies': profile.allergies,
                        'wallet': user.wallet_address
                    }]
                }
            if request.user.is_doctor:
                username = User.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                profile = DoctorInformation.objects.get(user=request.user)
                response = {
                    'success': 'true',
                    'status': status.HTTP_200_OK,
                    'message': 'Doctor Information successfully retrieved',
                    'data': [{
                        'name': username.name,
                        'hospital':profile.hospital_name,
                        'wallet': username.wallet_address
                    }]
                }
            if request.user.is_superuser:
                profile = User.objects.get(user = request.user)
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
    
class PrescriptionView(viewsets.ModelViewSet):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

""" class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = PatientInformation.objects.all()

class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = DoctorInformation.objects.all() """

""" class RegisterView(APIView):
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
 """