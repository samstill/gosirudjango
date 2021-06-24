from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UsersChangeForm, UsersCreationForm
from .models import Users

# # Register your models here.
Users = get_user_model()
class UsersAdmin(UserAdmin):
    add_form = UsersCreationForm
    form = UsersChangeForm
    model = Users
    list_display = ['username',"email", 'is_verified']


admin.site.register(Users, UsersAdmin)