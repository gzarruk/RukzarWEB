from django.db import models

# Create your models here.
class sesion(models.Model):
    actividad = models.CharField(max_length=264,
                                choices=(('NT', 'Natación'),
                                         ('CL', 'Ciclismo'),
                                         ('AT', 'Atletismo'),
                                         ('FZ', 'Fuerza'),
                                         ('DS', 'Descanso'),
                                         ('CD', 'Otra-Cardio')))
    nombre = models.CharField(max_length=264)
    tipo = models.CharField(max_length=264)
    duracion = models.FloatField(null=True,
                            default=None, verbose_name='Duración')
    duracion_unidad = models.CharField(max_length=3,
                                            choices=(('min', 'min'),
                                                     ('hr', 'hr'),
                                                     ('m', 'm'),
                                                     ('km', 'km')),
                                        verbose_name='Unidad de duración')
    zona = models.CharField(max_length=10,blank=True,
                                choices=(('Z1', '1'),
                                         ('Z2', '2'),
                                         ('Z3', '3'),
                                         ('Z4', '4'),
                                         ('Z5', '5')))
    descripcion = models.TextField(max_length=5000, verbose_name='Descripción')
    comentarios = models.TextField(max_length=5000,blank=True, verbose_name='Comentarios')
    periodo = models.CharField(max_length=10,blank=True,
                                choices=(('TO0', 'Todos'),
                                         ('BA0', 'Base'),
                                         ('PR0', 'Progresión'),
                                         ('ZE0', 'Zenít'),
                                         ('CO0', 'Competencia'),
                                         ('BP0', 'Base, Progresión'),
                                         ('BZ0', 'Base, Zenít'),
                                         ('BC0', 'Base, Competencia'),
                                         ('PZ0', 'Progresión, Zenít'),
                                         ('PC0', 'Progresión, Competencia'),
                                         ('ZC0', 'Zenít, Competencia'),
                                         ('BPZ', 'Base, Progresión, Zenít'),
                                         ('BPC', 'Base, Progresión, Competencia'),
                                         ('BZC', 'Base, Zenít, Competencia'),
                                         ('PZC', 'Progresión, Zenít, Competencia')))

    def __str__(self):
        return self.actividad + ": " + self.nombre + " (" + self.tipo + ")"
