from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name="base"),
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('productos/', productos, name="productos"),
    path('salir/', salir, name="salir"),
    path('acceder/', acceder, name="acceder"),
    path('contacto/', contacto, name="contacto"),
    
]
