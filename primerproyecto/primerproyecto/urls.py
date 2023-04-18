"""
URL configuration for primerproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from primero.views import index_principal, otra_pagina, pagina_persona
from primero.views import Pagina4View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_principal, name="index"),
    path('pagina2/', otra_pagina, name="otra"),
    path('pagina3/', TemplateView.as_view(template_name="otrapagina_sub.html"), name='otra2'),
    path('pagina4/', Pagina4View.as_view(), name='otra4'),
    path('persona/<int:id>', pagina_persona, name='persona')
]
