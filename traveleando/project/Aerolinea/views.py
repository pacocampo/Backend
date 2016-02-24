from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
def Aero(request):
	aerolineas = Aerolinea.objects.all()
	print(aerolineas)
	
	if request.method == "POST":
		aForm = AerolineaForm(request.POST)
		if aForm.is_valid():
			aForm.save()
		else:
			print(aForm.errors)
			return render(request, 'vuelos.html', {'aerolineas':aerolineas, 'form': AerolineaForm(request.POST)})
	else :
		return render(request, 'vuelos.html', {'aerolineas':aerolineas, 'form': AerolineaForm()})