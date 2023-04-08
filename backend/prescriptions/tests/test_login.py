from django.test import TestCase
from rest_framework.test import APITestCase
from prescriptions.models import PatientInformation, DoctorInformation, User

class AccountTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_patient(
            email="demo@example.com"
            password="12345"
        )

        self.user_2 = User.objects.create_doctor(
            email="abcd@g.com"
            password="1234"
        )
    
    def test_profile_created(self):
        profile = User.objects.count()
        self.assertEqual(profile, 2)