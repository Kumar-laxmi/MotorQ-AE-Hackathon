from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

role_choices = [
    ('admin', 'Admin'),
    ('participant', 'Participant')
]


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    role = forms.CharField(widget=forms.Select(choices=role_choices))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']