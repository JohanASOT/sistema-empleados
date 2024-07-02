from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewRegisterForm
from applications.empleados.models import Empleado
from .models import Departamento

# Create your views here.
class Departamentos(ListView):
    model = Departamento
    template_name = 'departamento/departamentos.html'
    context_object_name = 'departamentos'

class EmpleadoDepartamento(FormView):
    template_name = 'departamento/empleado-departamento.html'
    form_class = NewRegisterForm
    success_url = '/'

    def form_valid(self, form):
        print('-------------------------')
        # Maneras de recuperar datos desde el formulario

        # Opcion A:
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname'],
        )

        depa.save()

        # Opcion B
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '0',
            departamento = depa,
        )

        return super(EmpleadoDepartamento, self).form_valid(form)
    