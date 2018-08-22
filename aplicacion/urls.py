from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.inicio, name=''),
    path('pantalla1/', views.pantalla1, name=''),
    path('pantalla2/', views.pantalla2, name=''),
    path('salirSesion/',views.salir, name='')
]