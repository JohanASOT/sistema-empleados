from django import forms
from . models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = ('title', 'subtitle', 'cantidad',)
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'placeholder':'Ingresar el titulo'
                }
            ),
            'subtitle': forms.TextInput(
                attrs = {
                    'placeholder':'Ingresar el subtitulo'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'placeholder':'Cantidades mayores a 10'
                }
            )
        }

    # Validando el campo de cantidad con numeros mayores a 10.
    def clean_cantidad(self):

        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingresar numero mayor a 10.')

        return cantidad