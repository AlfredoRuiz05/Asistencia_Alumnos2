from django.db import models



class Categoria(models.Model):
    nombre = models.CharField()

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    categorias = models.ManyToManyField(Categoria)
    # ejemplo = models.OneToOneField()
    logo = models.ImageField(null=True, blank=True, upload_to="materias_logo/")

# Materia --> "Desarrollo web" ("informatica", "programacion")

