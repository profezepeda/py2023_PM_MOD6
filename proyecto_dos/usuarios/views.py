from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

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