#django
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

from mainapp.models import Furniture, FurnitureImage
#app
from .models import Furniture
from .forms import ContactForm


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
                form.cleaned_data["content"]  + "\n" + "\n" + form.cleaned_data["email"],#on saute une ligne entre l'email et le message
                "",#ici c'est l'email de celui qui donne mais c'est toujours moi cf settings (logique on peut pas envoyer de qq d'autre sans son mdp)
                ['clemencepavec@gmail.com'],
                fail_silently=False,
            )
            return redirect('index')#avec un message de succès
        form = ContactForm()#remise à blanc

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form} )

def portfolio_item_view(request, id_furniture):
    try:
        furniture = Furniture.objects.get(id=id_furniture)
        photos = FurnitureImage.objects.filter(furniture=furniture)
    except furniture.DoesNotExist:
        raise Http404

    #on ne met pas en meuble relié le meuble lui même d'où le if
    related_furnitures_ = Furniture.objects.filter(category = furniture.category, caracteristic = furniture.caracteristic)
    related_furnitures = []
    for el in related_furnitures_:
        if el != furniture:
            related_furnitures.append(el)


    #pour mettre une lettre sur 4 ou 5 jaune
    titre = []
    for i in range(len(furniture.title)):
        if i%5==1:
            titre.append((furniture.title[i].upper(), 'yellow'))
        else:
            titre.append((furniture.title[i].upper(), 'white'))

    return render(request,'portfolio_item.html',{'titre':titre,'furniture':furniture,  "related_furnitures":related_furnitures, "photos":photos})

