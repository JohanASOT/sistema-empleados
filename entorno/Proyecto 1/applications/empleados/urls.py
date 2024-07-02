from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('Inicio/', views.InicioView.as_view(), name='inicio'),
    path('listar-empleados/', views.ListAll.as_view(), name='listar-empleados'),
    path('empleado/<int:pk>/', views.ListEmployee.as_view(), name='empleado-detail'),
    path('administrar/', views.EmployeeAdmin.as_view(), name='empleados-admin'),

    path('listar-por-area/<shor_name>/', views.ListByArea.as_view(), name='empleados-area'),
    path('listar-por-trabajo/<job>/', views.ListByJob.as_view()),
    path('lista-por-palabra/', views.ListByKword.as_view()),
    path('lista-por-habilidad/<int:pk>/', views.ListBySkill.as_view()),
    path('registrar-empleado/', views.CreateEmployee.as_view(), name='crear-empleado'),
    path('registro-correcto/', views.SuccessCreateTemplate.as_view(), name='register-success'),
    path('editar-empleado/<int:pk>/', views.UpdateEmployee.as_view(), name='editar-empleado'),
    path('edicion-correcta/', views.SuccessEditTemplate.as_view(), name='update-success'),
    path('eliminar-empleado/<int:pk>/', views.DeleteEmployee.as_view(), name='eliminar-empleado'),
    path('eliminado-exitoso/', views.SuccessDeleteTemplate.as_view(), name='delete-success'),
]
