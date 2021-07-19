from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ContactoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})

    def post (self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, f"Bienvenido/a a la plataforma {nombre}")
            login(request, usuario)
            return redirect("base")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro", {"form": form})

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f"Bienvenido/a nuevamente {nombre}")
                return redirect("base")
            else:
                messages.error(request, "Los datos son incorrectos")
        else: 
            messages.error(request, "Los datos son incorrectos")       
    form = AuthenticationForm()
    return render(request, "acceder.html", {"form": form})

def salir(request):
    logout(request)
    messages.success(request, F"Sesión finalizada")
    return redirect("acceder")


def base(request):
    return render(request, "base.html")

def productos (request):
    return render(request, "productos.html")

def contacto(request):
    form = ContactoForm()
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, "contacto.html", context)
