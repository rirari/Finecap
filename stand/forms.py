from django import forms
from .models import Reserva
from django.forms import ModelForm

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa' : forms.Select(attrs={'class': 'form-control' }),
            'quitado' : forms.CheckboxInput(),
            'stand': forms.Select(attrs={'class': 'form-control' }),
        }

       