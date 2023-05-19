from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile, User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'is_manage', 'is_customer',)
