from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from .managers import UserManager

# Create your models here.
phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$",
                                 "The phone number provided is invalid")


class Roles(models.Model):
    """
    This model is used to distribute roles because some roles need to display all the content and some partially
    For Example
    role Administrator can see all content
    role a doctor can only see publications

    """
    name_of_roles = models.CharField(max_length=255)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = "Роли"

    @classmethod
    def get_default_pk(cls):
        # roles, create = cls.objects.get_or_create(
        #     name_of_roles = "roles"
        #     )
        return

    def __str__(self):
        return self.name_of_roles


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField("Адрес электронной почты", blank=False, null=False)
    phone_number = models.CharField("Номер телефона", max_length=20, validators=[phone_validator],
                                    blank=True, null=True)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    third_name = models.CharField("Отчество", max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    roles = models.ForeignKey(Roles, verbose_name="Группа пользователей", on_delete=models.DO_NOTHING)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        unique_together = ('username', 'email', 'phone_number')
