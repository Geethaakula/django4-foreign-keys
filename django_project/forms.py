from django.forms import ModelForm, HiddenInput
from .models import Input,Region
from .widget import DateTimePickerInput




class TicketForm(ModelForm):
    class Meta:
        model = Input
        fields = ['time', 'address', 'region', 'day']
        widgets = {
            "time": DateTimePickerInput(format='%m/%d/%y %H:%M:%S'),
            'day': HiddenInput()
        }