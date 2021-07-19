from django.forms import ModelForm
from .models import contacto

class ContactoForm(ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'