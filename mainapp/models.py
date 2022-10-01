from ast import keyword
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()

"""
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    
    def __str__(self):
        return "Message de {}".format(self.name)
"""

class Furniture(models.Model):
	title = models.CharField(max_length=35, verbose_name='titre (30 caractère max')
	image =  models.ImageField(null=True, blank=True, verbose_name='image_liste (plutot carré)')
	description = models.TextField(verbose_name = 'description', null=True, blank=True)
	date = models.DateTimeField(default=now, blank=True)
	keywords = models.CharField(null=True, max_length=255, verbose_name='mots clé à afficher en plus de catgorie et caractérisitique', blank=True)
	for_sale = models.BooleanField()
	category = models.CharField(max_length=42, verbose_name='catégorie : creation/restauration') #faire un form avec une liste déroulante avec restauration/création
	caracteristic = models.CharField(max_length=255, verbose_name='caractéristiques : massif plaque // marqueterie sculpture boite_et_coffret jeux meuble_a_secret') #faire de même un forme déroulant
	price = models.IntegerField(null=True, blank=True) #si pas à vendre pas de prix
	#Mettre peut-être d'autres images avec charfield image

	def __str__(self):
		return "{}".format(self.title)

class FurnitureImage(models.Model):
    furniture = models.ForeignKey(Furniture, default=None, on_delete=models.CASCADE)
    images = models.FileField(verbose_name='Images item plutot rectangulaire')#Upload_to = 'images/'
 
    def __str__(self):
        return self.furniture.title

