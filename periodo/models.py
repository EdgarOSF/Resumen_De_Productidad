from django.db import models
from django.urls import reverse_lazy

from tribunal.models import Tribunal


class Periodo (models.Model):
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_termino = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    fk_tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Periodo'
        verbose_name = "periodo"
        ordering = ['fecha_inicio']
        verbose_name_plural = "periodos"

    def __str__(self):
        return f'{self.fecha_inicio} - {self.fk_tribunal}'
    
    def get_absolute_url(self):
        return reverse_lazy('periodo:detail', kwargs={'pk': self.id})

