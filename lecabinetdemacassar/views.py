from django.shortcuts import render
from mainapp.models import Furniture
#simple function which return the index page
def index(request):
	furnitures = Furniture.objects.order_by('date').all()[:4]
	return render(request, 'index.html', {'furnitures':furnitures})

