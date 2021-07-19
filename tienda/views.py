from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse

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
            return render(request, "registro.html", {"form": form})

def base(request):
    return render(request, "base.html")

