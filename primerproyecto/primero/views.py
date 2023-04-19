from django.shortcuts import render
from django.views.generic import TemplateView

from primero.forms.formulariocontacto import FormularioContactoForm

lista_personas = [
    { "id": 1, "nombre": "maria", "apellido": "gomez", "edad": 25 },
    { "id": 2, "nombre": "josé", "apellido": "gonzalez", "edad": 25 },
    { "id": 3, "nombre": "mario", "apellido": "perez", "edad": 25 },
    { "id": 4, "nombre": "josefa", "apellido": "perez", "edad": 25 },
    { "id": 5, "nombre": "pedro", "apellido": "martinez", "edad": 25 }]
contenido = "lore ipsum dolor sit amet, consectetur adipiscing elit."

# Create your views here.

def pagina_persona(request, id):
    for persona in lista_personas:
        if persona["id"] == id:
            return render(request, 'persona.html', {"persona": persona})
    return render(request, 'persona.html', {"persona": {
        "nombre": "no encontrado",
        "apellido": "!!",
    }})

def index_principal(request):
    # return render(request, 'index.html')
    return render(request, 'index_sub.html')

def otra_pagina(request):
    # return render(request, 'otrapagina.html')}
    persona = {
        "nombre": "juan",
        "apellido": "perez",
        "edad": 30
    }
    return render(request, 'otrapagina_sub.html', 
        {"persona": persona, "personas": lista_personas, "contenido": contenido})

# def formulario_contacto(request):
#     formulario = FormularioContactoForm()
#     context = { "formulario": formulario }
#     return render(request, 'formulariocontacto2.html', { "context": context})

class FormularioContactoView(TemplateView):
    template_name = "formulariocontacto3.html"

    def get_context_data(self, **kwargs):
        context = super(FormularioContactoView, self).get_context_data(**kwargs)
        context["formulario"] = FormularioContactoForm()
        return context


class Pagina4View(TemplateView):
    template_name = "otrapagina_sub.html"