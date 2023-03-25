"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prescriptions import views
from prescriptions.views import index

router = routers.DefaultRouter()
router.register(r'prescriptions', views.PrescriptionView, 'prescription')
router.register(r'patients', views.PatientView, 'patient')
router.register(r'doctors', views.DoctorView, 'doctor')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", include("django_nextjs.urls")),
    path("", index, name="index")
]
