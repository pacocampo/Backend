from django.shortcuts import render
from .models import Destino
# Create your views here.
def index(request):
	d =  Destino.mexico.all()
	return render(request, 'index.html', {'destinos':d})
