from django.db import models
from category.models import *
from usuario.models import *
from utils.countryinfo import COUNTRY_CHOICES
# Create your models here.
class MexicoManager(models.Manager):
    def get_queryset(self):
        return super(MexicoManager, self).get_queryset().filter(pais='MX')


class Destino(models.Model):

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    #Relations
    categoria = models.ForeignKey(Category)

    #Attributes
    nombre = models.CharField(max_length=100, blank=False)
    pais = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    continente = models.CharField(max_length=15, blank=False)
    imagen = models.ImageField(upload_to='media/pais/')
    is_active = models.BooleanField(default=True)

    #Manager
    object = models.Manager()
    mexico = MexicoManager()

    def __str__(self):
        return self.nombre
   
