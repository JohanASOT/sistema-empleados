from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class ResumeFoundation(TemplateView):
    template_name = 'home/resume-foundation.html'

class PruebaListView(ListView):
    template_name = 'home/lista_prueba.html'
    queryset = ['a', 'b', 'c']
    context_object_name = 'prueba_lista'

class PruebaLista(ListView):
    model = Prueba
    template_name = 'home/lista.html'
    context_object_name = 'pruebas'

class PruebaAdd(CreateView):
    model = Prueba
    template_name = 'home/add-prueba.html'
    form_class = PruebaForm
    success_url = '/'