from django.contrib import admin
from django.urls import path
from persona.views import * 


urlpatterns = [
    path('',index, name='index'),
    path('listado/',listado, name='listado'),
    path('nueva/',nueva, name='nueva'),
    path('editar/<int:id>',editar, name='editar'),
    path('contacto/', contacto, name='contacto'),
    path('persona_paginacion/',persona_paginacion,name='persona_paginacion')
]


