from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from usuarios.forms.ingresoForm import FormularioLogin

# Create your views here.

def indexpage(request):
  return render(request, "index.html")

class UsuariosPage(TemplateView):
  template_name = "usuarios.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["usuarios"] = User.objects.all()
    usuario = User.objects.get(id=1)
    usuario = User.objects.get(username="marcelo")
    usuario = User.objects.get(email="jperez@juanito.org")
    print(usuario)
    return context

def loginusuario(request):
  if request.method == "GET":
    form = FormularioLogin()
  if request.method == "POST":
    form = FormularioLogin(request.POST)
    if form.is_valid():
      usuario = form.cleaned_data["usuario"]
      password = form.cleaned_data["password"]
      user = authenticate(username=usuario, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect("usuarios")
        else:
          form.errors["usuario"] = "Usuario no válido"
      else:
        form.errors["usuario"] = "Usuario no válido"
    else:
      form.errors["usuario"] = "Usuario no válido"
  return render(request, "registration/login.html", {'form':form})

from django.contrib.auth.models import Group, User

