from django import forms
from .models import Gifts


class GiftsForm(forms.ModelForm):
    class Meta:
        model = Gifts
        fields =['gift']
       
    





    
    