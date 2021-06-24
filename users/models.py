from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Create your models here.

class Users(AbstractUser):
    mobile_number = PhoneNumberField()
