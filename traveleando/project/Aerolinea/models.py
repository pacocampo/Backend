from django.db import models
from usuario.models import MyUser
from destino.models import Destino
from utils.countryinfo import COUNTRY_CHOICES
# Aerolineas
#ModelManager
class AerolineaManager(models.Manager):
  def queryset(self):
    return super().get_query_set().filter(is_active=True)


#Model
class Aerolinea(models.Model):

    class Meta:
        verbose_name = "Aerolinea"
        verbose_name_plural = "Aerolineas"

    #Attributes
    nombre = models.CharField(max_length=60, blank=False)
    pais = models.CharField(max_length=2, choices= COUNTRY_CHOICES)
    is_active = models.BooleanField(default=True)

    #Manager
    object = models.Manager()
    activas = AerolineaManager()
    
    def __str__(self):
        return self.nombre
    
class Vuelo(models.Model):

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"

    #Relations
    aerolinea = models.ForeignKey(Aerolinea)
    destino = models.ForeignKey(Destino)

    #Attributes
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return (self.aerolinea.nombre + " " + self.destino.nombre) 

#Bitacora de vuelos
class Bitacora(models.Model):
  
      class Meta:
          verbose_name = "Bitacora"
          verbose_name_plural = "Bitacoras"

      #Relations
      usuario = models.ForeignKey(MyUser)
      vuelo = models.ForeignKey(Vuelo)
  
      def __str__(self):
          return (self.usuario.user.first_name + " " + self.usuario.user.last_name + " viajo a " + self.vuelo.destino.nombre)


        