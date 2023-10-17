from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from . import models

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        #model = models.Profile
        fields =['username', 'email', 'password1', 'password2']

class EditUserForm (UserChangeForm):
    class Meta:
        model = User
        #model = models.Profile
        fields=('username','first_name','last_name','email')

class UserChangePassword(PasswordChangeForm):
    class Meta:
        #model = User
        model = models.Profile
        fields =['password1', 'password2']