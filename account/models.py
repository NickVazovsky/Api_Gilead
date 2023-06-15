from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator


# Create your models here.
phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, third_name, phone_number, password=None):
        if not email:
            raise ValueError('User email is required field')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, third_name=third_name,
                          phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамалия", max_length=100)
    third_name = models.CharField("Отчество", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20, validators=[phone_validator], unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
