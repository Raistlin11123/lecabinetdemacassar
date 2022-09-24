from ast import keyword
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
	title = models.CharField(max_length=255, verbose_name='titre')
	image =  models.ImageField(null=True, blank=True, verbose_name='image')
	description = models.TextField(verbose_name = 'description', null=True, blank=True)
	date = models.DateTimeField(default=now, blank=True)
	keywords = models.CharField(null=True, max_length=255, verbose_name='mots clé', blank=True)
	for_sale = models.BooleanField()
	category = models.CharField(max_length=42, verbose_name='catégorie') #faire un form avec une liste déroulante avec restauration/création
	caracteristic = models.CharField(max_length=255, verbose_name='caractéristiques') #faire de même un forme déroulant
	price = models.IntegerField(null=True, blank=True) #si pas à vendre pas de prix
	#Mettre peut-être d'autres images avec charfield image

	def __str__(self):
		return "{}".format(self.title)

