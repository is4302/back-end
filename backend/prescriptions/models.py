from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class PatientInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=id, related_name='patient')
    name = models.TextField()
    dob = models.DateField('Date of Birth')
    height = models.BigIntegerField()
    weight = models.FloatField()
    history = models.JSONField()
    allergies = models.TextField()
    patient_wallet = models.CharField(max_length=255)
    
    def __str__(self):
        return self.patient_wallet

class DoctorInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=id, related_name='doctor')
    name = models.TextField()
    hospital_name = models.TextField()
    doctor_wallet = models.CharField(max_length=255)

    def __str__(self):
        return self.doctor_wallet

class Prescription(models.Model):
    date =  models.DateField('Date of Prescription')
    patient = models.OneToOneField(PatientInformation, on_delete=models.CASCADE)
    doctor = models.OneToOneField(DoctorInformation, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    rand_id = models.BigIntegerField()

class Appointment(models.Model):
    appointment_time = models.DateTimeField('Appointment Time')
    patient = models.OneToOneField(PatientInformation, on_delete=models.CASCADE)
    doctor = models.OneToOneField(DoctorInformation, on_delete=models.CASCADE)



