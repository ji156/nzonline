from django.db import models
from django.conf import settings

# Create your models here.


class Cursos(models.Model):
    CATEGORIAS = [
        ('Desarrollo Web', 'Desarrollo Web'),
        ('Diseño Gráfico', 'Diseño Gráfico'),
        ('Programación', 'Programación'),

        # Agrega más categorías según sea necesario
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    precio_oferta = models.IntegerField()
    imagen = models.ImageField(upload_to='cursos_imagenes/')
    fecha = models.DateField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    estado = models.BooleanField(default=True)
    autor = models.CharField(max_length=50)
    puntuacion = models.IntegerField(
        choices=[(i, str(i)) for i in range(6)])  # Valores de 0 a 5

    def __str__(self):
        return self.nombre
