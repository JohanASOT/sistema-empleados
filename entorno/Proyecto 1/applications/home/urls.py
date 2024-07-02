from django.urls import path
from . import views

urlpatterns = [
    path('prototipo', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.PruebaLista.as_view()),
    path('añadir-prueba/', views.PruebaAdd.as_view(), name='prueba-add'),
    path('resume-foundation/', views.ResumeFoundation.as_view(), name='foundation'),
]