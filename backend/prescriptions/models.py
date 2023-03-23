from django.db import models

class Prescription(models.Model):
    patient_id = models.BigIntegerField()
    doctor_id = models.BigIntegerField()
    prescription_desc = models.TextField()
    hash_id = models.CharField(max_length=255)


class PatientInformation(models.Model):
    name = models.TextField()
    dob = models.DateField('Date of Birth')
    height = models.BigIntegerField()
    weight = models.BigIntegerField()
    history = models.TextField()
    allergies = models.TextField()
    patient_id = models.BigIntegerField()

class DoctorInformation(models.Model):
    name = models.TextField()
    hospital_name = models.TextField()
    doctor_id = models.BigIntegerField()
