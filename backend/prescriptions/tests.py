from django.test import TestCase
from prescriptions.models import User
import json

test_users = [
    {"username": "testuser1", "password": "testpassword1"},
    {"username": "testuser2", "password": "testpassword2"},
]

class LoginTest(TestCase):
    def setUp(self):
        for user in test_users:
            new_user = User.objects.create(username=user["username"])
            new_user.set_password(user["password"])
            new_user.save()

class AccountTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_patient(
            name="Jack",
            email="demo@example.com",
            wallet_address="0xabcd",
            password="12345",
            dob="1900-01-01",
            height="200",
            weight="100",
            history={"serious": ["dead"]},
            allergies="Penicillin, Danger"
        )

        self.user_2 = User.objects.create_doctor(
            name="James",
            email="abcd@g.com",
            wallet_address="0xasdas",
            hospital_name="Jon Hospital",
            password="1234"
        )
    
    def test_profile_created(self):
        profile = User.objects.count()
        self.assertEqual(profile, 2)