from django import forms
from .models import User,Gifts




# class RegisterForm(forms.Form):
#     email = forms.EmailField(max_length=30)
#     username = forms.CharField(max_length=25)
#     password = forms.CharField(max_length=15)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['email','username', 'password']
        widgets = {'password': forms.PasswordInput()
         }
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)

class GiftsForm(forms.ModelForm):
    class Meta:
        model = Gifts
        fields =['gift']
       
    





    
    