from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField("Nombres", max_length=80)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libros(models.Model):
    title = models.CharField("titulo", max_length=150)
    resume = models.TextField("resumen")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    