from django.db import models

class Prescription(models.Model):
    patient_id = models.BigIntegerField()
    doctor_id = models.BigIntegerField()
    prescription_desc = models.CharField()
    hash_id = models.CharField()


class PatientInformation(models.Model):
    patient_name = models.CharField()
    patient_dob = models.DateTimeField('Date of Birth')
    patient_height = models.BigIntegerField()
    patient_weight = models.BigIntegerField()
    patient_history = models.CharField()
    patient_allergies = models.CharField()
    patient_id = models.BigIntegerField()

class DoctorInformation(models.Model):
    doctor_name = models.CharField()
    doctor_hospital_name = models.CharField()
    doctor_id = models.BigIntegerField()

