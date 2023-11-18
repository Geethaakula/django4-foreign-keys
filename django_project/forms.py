from django.db.models.base import Model
from django.forms import ModelForm, HiddenInput,ModelChoiceField,Select
from .models import Input,Region
from .widget import DateTimePickerInput


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