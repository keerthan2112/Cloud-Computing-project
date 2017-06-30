from django import forms

from django.contrib.auth.models import User

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())


class CreateForm(forms.Form):
   username = forms.CharField(max_length = 100)
   email = forms.CharField(max_length= 100)
   password = forms.CharField(widget = forms.PasswordInput())