from tkinter import Widget
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'catidad',
        )
        widgets={
             'titulo': forms.TextInput(
                  attrs={
                       'placeholder': 'Ingrese texto aqui'
                  }
             )
        }

    def clean_catidad(self):
            cantidad= self.cleaned_data['catidad']
            if cantidad<10:
                raise forms.ValidationError('Ingrese un numero mayor a 10')
            return cantidad
