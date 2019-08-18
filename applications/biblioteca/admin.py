from django.contrib import admin

# Register your models here.
from .models import Autor, Libros


class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    #atributo para buscar por un campo
    search_fields = ('nombre', 'nacionalidad',)

class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'autor',
        'id'
    )
        #atributo para buscar por un campo
    search_fields = ('title', 'autor',)

    #para hacer filtros
    list_filter = ("autor",)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)