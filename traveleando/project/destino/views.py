from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	d = Destino.mexico.all()
	print(d)
	return render(request,'home/index.html',{'destinos':d})