from django.urls import path
from .views import VistaRegistro, base

urlpatterns = [
    path('', base, name="base"),
    path('registro/', VistaRegistro.as_view(), name="registro"),
    
]
