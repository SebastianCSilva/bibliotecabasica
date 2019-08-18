from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)
from . models import Autor, Libros


class ListaAutores(ListView):
    template_name = 'biblioteca/lista-autores.html'
    model = Autor
    context_object_name = 'autores'

class ListaLibrosAutores(ListView):
    template_name = 'biblioteca/lista-libros.html'
    #model = Libros
    context_object_name = 'libros'

    def get_queryset(self):
        #identificar autor + filtros + return
        id = self.kwargs['pk']

        lista = Libros.objects.filter(
            autor = id
        )
        return lista
    
class AddAutor(CreateView):
    #Vista para la creacion de autores
    template_name = 'biblioteca/add-autor.html'
    model = Autor
    fields = ['nombre','nacionalidad']
    success_url = 'add'