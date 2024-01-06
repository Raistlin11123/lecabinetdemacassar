from django.shortcuts import render
from mainapp.models import Furniture
#simple function which return the index page
def index(request):
	furnitures = Furniture.objects.order_by('date').all()[:4]
	return render(request, 'index.html', {'furnitures':furnitures})

def politique_de_confidentialite(request):
	return render(request, 'politique_de_confidentialite.html')

def mentions_legales(request):
	return render(request, 'mentions_legales.html')
