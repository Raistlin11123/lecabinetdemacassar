#django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

from mainapp.models import Furniture
#app
from .models import Furniture
from .forms import ContactForm


send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)




def portfolio_creation_view(request):
    furnitures = Furniture.objects.filter(category = "creation")
    return render(request, 'portfolio_creation.html', {'furnitures':furnitures})

    
def portfolio_restauration_view(request):
    furnitures = Furniture.objects.filter(category = "restauration")
    return render(request, 'portfolio_restauration.html', {'furnitures':furnitures})

def contact_view(request):
    #Formulaire pour un nouvel indice
    if request.method == "POST":
        form = ContactForm(request.POST)
        #si le formulaire est valide,
        if form.is_valid():
            #si la réponse est correcte
            #(On peut ajouter des conditions pour vérifier que le message est bien)
            send_mail(
                form.cleaned_data["subject"],
                form.cleaned_data["content"],
                form.cleaned_data["email"],
                ['philippepavec@gmail.com'],
                fail_silently=False,
            )
            return redirect('index')#avec un message de succès
            

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form} )