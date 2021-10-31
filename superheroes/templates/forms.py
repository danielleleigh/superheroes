from django.forms import ModelForm
from models import Superhero

class EditSuperhero(ModelForm):
    class Meta:
        model = Superhero
        fields = '__all__'