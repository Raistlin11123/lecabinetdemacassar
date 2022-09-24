from django.shortcuts import render

#simple function which return the index page
def index(request):
	return render(request, 'index.html', locals())