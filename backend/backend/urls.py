from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prescriptions.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path("api/signup/patient", PatientRegistrationView.as_view(), name='patient_signup'),
    path("api/signup/doctor", DoctorRegistrationView.as_view(), name='doctor_signup'),
    path("api/login", UserLoginView.as_view()),
    path("api/profile", ProfileView.as_view()),
    path("api/appointment", AppointmentView.as_view()),
    path("api/appointment/doctor", AppointmentGetDoctorView.as_view()),
    path("api/prescription", PrescriptionView.as_view()),
    path("api/list/doctor", GetDoctorView.as_view()),
    path("api/list/patient", GetPatientView.as_view())
]

