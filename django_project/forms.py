from django.db.models.base import Model
from django.forms import ModelForm, HiddenInput,ModelChoiceField,Select
from .models import Input,Region
from .widget import DateTimePickerInput
from django import forms


class TicketForm(ModelForm):
    class Meta:
        model = Input
        fields = ['time', 'address', 'region', 'day']
        widgets = {
            "time": DateTimePickerInput(format='%m/%d/%y %H:%M:%S'),
            'day': HiddenInput(),
        }
    region = ModelChoiceField(queryset=Region.objects.all(),to_field_name='name',required=True,
                              widget=Select)
    
class DayForm(forms.Form):
    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    REGION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
    ]

    region = forms.ChoiceField(choices=REGION_CHOICES)

    day = forms.ChoiceField(choices=DAYS_CHOICES)
    
    