from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('departamentos/', views.Departamentos.as_view(), name='departamentos'),
    path('empleado-departamento/', views.EmpleadoDepartamento.as_view(), name='empleado-departamento'),
]
