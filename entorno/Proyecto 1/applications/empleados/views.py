from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm


# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'

# 1. Listar todos los empleados del modelo
class ListAll(ListView):
    template_name = 'empleados/list_all.html'
    ordering = ('id') # Puedo ordenar tanto en views.py como en models.py
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave,
        )
        print (lista)
        return lista

class ListEmployee(DetailView):
    model = Empleado
    template_name = 'empleados/empleado.html'

# 2. Listar los empleados que pertenecen a un area de trabajo
class ListByArea(ListView):
    template_name = 'empleados/list-area.html'
    ordering = ('id')
    context_object_name = 'empleados'
    #queryset = Empleado.objects.filter(departamento__shor_name='Contaduría') # Filtrar datos por queryset -- No tan recomendada --

    # Filtar datos interactuando con la URL del navegador
    def get_queryset(self):
        
        area = self.kwargs['shor_name']
        lista = Empleado.objects.filter(departamento__shor_name=area)
        return lista

# 3. Listar empleados por trabajo
class ListByJob(ListView):
    template_name = 'empleados/list-job.html'
    ordering = ('-id')

    # Filtrar datos utilizando el metodo GET mediante la URL
    def get_queryset(self):

        job = self.kwargs['job'] # Acceder a los JOB_CHOICES mediante el id del campo: job
        lista = Empleado.objects.filter(job=job)
        return lista

# 4. Listar empleados por palabra clave
class ListByKword(ListView):
    template_name = 'empleados/list-by-kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        palabra_clave = self.request.GET.get('kword')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        print (lista)
        return lista

class ListBySkill(DetailView):
    model = Empleado
    template_name = 'empleados/list-by-skill.html'
    context_object_name = 'empleado'


class EmployeeAdmin(ListView):
    model = Empleado
    template_name = 'empleados/admin-list.html'
    context_object_name = 'empleados'
    paginate_by = 10
    ordering = ('id')


class CreateEmployee(CreateView):
    model = Empleado
    template_name = 'empleados/create-employee.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados-admin')

    def form_valid(self, form):

        empleado = form.save()
        empleado.full_name = f"{empleado.first_name} {empleado.last_name}"
        empleado.save()
        return super(CreateEmployee, self).form_valid(form)

class SuccessCreateTemplate(TemplateView):
    template_name = 'empleados/success.html'

class UpdateEmployee(UpdateView):
    model = Empleado
    template_name = 'empleados/editar-empleado.html'
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades',]
    success_url = reverse_lazy('empleados_app:empleados-admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('----- Metodo POST -------')
        print(request.POST) # Interceptar valores desde la URL con el metodo post antes de que sean enviados y validados
        print('Con el metodo post estoy tomando el valor del campo first_name de mi BD:', request.POST['first_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('---------- Metodo form_valid ---------------')
        print('Se ejecuta despues del metodo post')
        return super().form_valid(form)

class SuccessEditTemplate(TemplateView):
    template_name = 'empleados/success-edit.html'

class DeleteEmployee(DeleteView):
    model = Empleado
    template_name = 'empleados/delete-empleado.html'
    success_url = reverse_lazy('empleados_app:empleados-admin')

class SuccessDeleteTemplate(TemplateView):
    template_name = 'empleados/success-delete.html'