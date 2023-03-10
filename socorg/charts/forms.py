from django import forms
from .models import Persona


class CreateEgoForm(forms.Form):
    model = Persona
    chart = forms.CharField(label="Name of the Chart", max_length=200, required=False)
    name = forms.CharField(label="Name", max_length=50)
    surname = forms.CharField(label="Surname", max_length=50)
