from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff = False, is_superuser=False) -> "User":
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None) -> "User":
        user = self.create_user(email = email,
                                password = password,
                                is_staff = True,
                                is_superuser = True)
        user.save()
        return self.create_user(email, password)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email', max_length=255)
    password = models.CharField(max_length=255, verbose_name='Password')
    username = None

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
