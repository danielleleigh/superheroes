from django import forms
from django.forms import ModelForm, widgets, fields
from .models import Superhero


class EditSuperhero(ModelForm):
    class Meta:
        model = Superhero
        fields = '__all__'
        
