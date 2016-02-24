from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
def index(request):
	d = Destino.mexico.all()

	if request.method == "POST":
		print("entre a post")
		form = DestinoForm(request.POST)
		if form.is_valid():
			newDestino = form.save()
			print(newDestino)
			return HttpResponseRedirect('/thanks/')
		else:
			messages.error(request, "Error")
		# if form.is_valid():
		# 	print(form)
		# 	destino = form.save(commit=False)
		# 	destino.nombre = form.cleaned_data['nombre']
		# 	destino.pais = form.cleaned_data['pais']
		# 	destino.continente = form.cleaned_data['continente']
		# 	destino.imagen = form['imagen']
		# 	destino.is_active = form['is_active']
		# 	print(destino)
		# 	destino.save()
		# else :
		# 	print("form no valid")

	return render(request, 'index.html', {'destinos':d, 'form': DestinoForm()})