import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    dob = models.DateField('Date of Birth')
    height = models.PositiveBigIntegerField()
    weight = models.FloatField()
    history = models.JSONField()
    allergies = models.TextField()
    patient_wallet = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    hospital_name = models.TextField()
    doctor_wallet = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username