from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model



class UsersCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username","email", "mobile_number")

class UsersChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")