from django import forms
from .models import *
class AerolineaForm(forms.ModelForm):
	class Meta:
		model = Aerolinea
		fields = ['nombre', 'pais']
			