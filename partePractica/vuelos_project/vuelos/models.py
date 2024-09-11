from django.db import models

class Vuelo(models.Model):
    TIPOS_VUELO = [
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPOS_VUELO)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
