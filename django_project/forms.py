from django import forms
from .models import Gifts, MyUser


class GiftsForm(forms.ModelForm):
    class Meta:
        model = Gifts
        fields =['gift']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields =['username', 'password']

class AuthForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)

    





    
    