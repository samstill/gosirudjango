from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class UsersCreationForm(UserCreationForm):
    mobile_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN'))
    class Meta:
        model = get_user_model()
        fields = ("username","email", "mobile_number")

class UsersChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")