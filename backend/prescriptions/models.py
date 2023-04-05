from django.db import models
from django.conf import settings

class PatientInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=id)
    name = models.TextField()
    dob = models.DateField('Date of Birth')
    height = models.BigIntegerField()
    weight = models.FloatField()
    history = models.JSONField()
    allergies = models.TextField()
    patient_wallet = models.CharField(max_length=255)

class DoctorInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=id)
    name = models.TextField()
    hospital_name = models.TextField()
    doctor_wallet = models.CharField(max_length=255)

class Prescription(models.Model):
    date =  models.DateField('Date of Prescription')
    patient = models.OneToOneField(PatientInformation, on_delete=models.CASCADE)
    doctor = models.OneToOneField(DoctorInformation, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    rand_id = models.BigIntegerField()

class Appointment(models.Model):
    appointment_time = models.DateTimeField()
    patient = models.OneToOneField(PatientInformation, on_delete=models.CASCADE)
    doctor = models.OneToOneField(DoctorInformation, on_delete=models.CASCADE)



