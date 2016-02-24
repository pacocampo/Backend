from django import forms
from .models import Destino

class DestinoForm(forms.ModelForm):
	class Meta:
		model = Destino
		fields = ['nombre', 'pais', 'continente', 'imagen', 'categoria', 'is_active']

		# widgets = {
  #           'nombre': forms.TextInput(
  #               attrs={'id': 'nombre', 'required': True, 'placeholder': 'Nombre', 'class': 'news__txt'}
  #           ),
  #       }