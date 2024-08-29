from django import forms # type: ignore
from .models import pacie

class pacienteForm(forms.ModelForm):
    class Meta:
        model = pacie
        fields = ['dni','nombre','apellido','edad','fecha_nacimiento','email','direccion','telefono']
