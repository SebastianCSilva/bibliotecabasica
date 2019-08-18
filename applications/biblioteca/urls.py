from django.urls import include, path, re_path

from . import views

app_name="biblioteca_app"

urlpatterns = [
    path('autores', views.ListaAutores.as_view(), name="lista-autores"),
    path('libros-autor/<pk>/', views.ListaLibrosAutores.as_view(), name="lista-libros"),
    path('autor/add', views.AddAutor.as_view(), name="autor-add"),

]
