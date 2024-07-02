from django import forms

class NewRegisterForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Nombre del empleado'}))
    apellidos = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder':'Apellidos del empleado'}))
    departamento = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Nombre del Departamento'}))
    shorname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Abreviatura'}))

    class Meta:
        fields = ('nombre', 'apellidos', 'departamento', 'shorname',)
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder':'Nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'placeholder':'Apellidos'
                }
            )
        }