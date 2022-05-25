from django import forms
from sqlalchemy import values 
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 50, label= "Username")
    password = forms.CharField(max_length=20, label="Password",widget= forms.PasswordInput)
    confirm = forms.CharField(max_length= 20, label= "Confirm Password", widget= forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        checkusers = User.objects.all()
 
        for a in checkusers:
            if str(a) == username:
                raise forms.ValidationError("This username already exists, please try another !")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match")

        values = {
            "username" : username,
            "password" : password,
        }
        return values