from django.db import models
from usuario.models import MyUser
from destino.models import Destino
from utils.countryinfo import COUNTRY_CHOICES
# Aerolineas
class Aerolinea(models.Model):

    class Meta:
        verbose_name = "Aerolinea"
        verbose_name_plural = "Aerolineas"

    #Attributes
    nombre = models.CharField(max_length=60, blank=False)
    pais = models.CharField(max_length=2, choices= COUNTRY_CHOICES)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Vuelo(models.Model):

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"

    #Relations
    aerolinea = models.ForeignKey(Aerolinea)
    destino = models.OneToOneField(Destino)

    #Attributes
    fecha = models.DateField(auto_now_add=False, blank=False)
    hora = models.TimeField(auto_now_add=False, blank=False)

    def __str__(self):
        return (self.aerolinea.nombre + " " + self.destino.nombre) 

#Bitacora de vuelos
class Bitacora(models.Model):
  
      class Meta:
          verbose_name = "Bitacora"
          verbose_name_plural = "Bitacoras"

      #Relations
      usuario = models.OneToOneField(MyUser)
      vuelo = models.OneToOneField(Vuelo)
  
      def __str__(self):
          return self.usuario
        