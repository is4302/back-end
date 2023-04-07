import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, email, wallet_address, password=None):
        if name is None:
            raise TypeError('Users must have a name')
        if email is None:
            raise TypeError('Users must have an email')
        if wallet_address is None:
            raise TypeError('Users must have a wallet address')
        user = self.model(name=name, email=self.normalize_email(email), wallet_address=wallet_address)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_doctor(self, name, email, wallet_address, hospital_name, password=None):
        user = self.create_user(name, email, wallet_address, password)
        user.is_doctor = True
        doctor_profile = DoctorInformation(user=user, hospital_name=hospital_name)
        doctor_profile.save(using=self._db)
    
    def create_patient(self, name, email, wallet_address, dob, height, weight, history, allergies, password=None):
        user = self.create_user(name, email, wallet_address, password)
        user.is_patient = True
        patient_profile = PatientInformation(user=user, dob=dob, height=height, weight=weight, history=history, allergies=allergies)
        patient_profile.save(using=self._db)
    
    def create_superuser(self, name, email, wallet_address, password=None):
        user = self.create_user(name, email, wallet_address, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUID(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    wallet_address = models.CharField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'wallet_address']

    objects = UserManager()
    
    def __str__(self):
        return self.email

class PatientInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=id, related_name='patient')
    # name = models.TextField()
    dob = models.DateField('Date of Birth')
    height = models.BigIntegerField()
    weight = models.FloatField()
    history = models.JSONField()
    allergies = models.TextField()
    # patient_wallet = models.CharField(max_length=255)
    
    def __str__(self):
        return self.patient_wallet

class DoctorInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=id, related_name='doctor')
    # name = models.TextField()
    hospital_name = models.TextField()
    # doctor_wallet = models.CharField(max_length=255)

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



